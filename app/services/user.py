from typing import Any, Awaitable, Callable, Optional, cast

from aiogram.types import User as AiogramUser
from aiogram_i18n.cores import BaseCore
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from tonutils.client import TonapiClient
from tonutils.wallet import WalletV5R1

from app.models.config import AppConfig
from app.models.dto import UserDto
from app.models.sql import User
from app.services.database import RedisRepository, SQLSessionContext


class UserService:
    session_pool: async_sessionmaker[AsyncSession]
    redis: RedisRepository
    config: AppConfig
    tonapi: TonapiClient

    def __init__(
        self,
        session_pool: async_sessionmaker[AsyncSession],
        redis: RedisRepository,
        config: AppConfig,
        tonapi: TonapiClient,
    ) -> None:
        self.session_pool = session_pool
        self.redis = redis
        self.config = config
        self.tonapi = tonapi

    async def create(
        self,
        aiogram_user: AiogramUser,
        i18n_core: BaseCore[Any],
    ) -> UserDto:
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            user: User = User(
                telegram_id=aiogram_user.id,
                name=aiogram_user.full_name,
                locale=(
                    aiogram_user.language_code
                    if aiogram_user.language_code in i18n_core.locales
                    else cast(str, i18n_core.default_locale)
                ),
            )
            await uow.commit(user)
        return user.dto()

    async def _get(
        self,
        getter: Callable[[Any], Awaitable[Optional[User]]],
        key: Any,
    ) -> Optional[UserDto]:
        user_dto: Optional[UserDto] = await self.redis.get_user(key=key)
        if user_dto is not None:
            return user_dto
        user: Optional[User] = await getter(key)
        if user is None:
            return None
        await self.redis.save_user(
            key=user.telegram_id,
            value=(user_dto := user.dto()),
            cache_time=self.config.common.users_cache_time,
        )
        return user_dto

    async def get(self, user_id: int) -> Optional[UserDto]:
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.users.get, user_id)

    async def by_tg_id(self, telegram_id: int) -> Optional[UserDto]:
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            return await self._get(repository.users.by_tg_id, telegram_id)

    async def update(self, user: UserDto, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(user, key, value)
        async with SQLSessionContext(self.session_pool) as (repository, uow):
            await repository.users.update(user_id=user.id, **user.model_state)
        await self.redis.save_user(
            key=user.telegram_id,
            value=user,
            cache_time=self.config.common.users_cache_time,
        )

    async def get_wallet(self, user: UserDto) -> WalletV5R1:
        if user.wallet_connected:
            wallet, public_key, private_key, mnemonic = WalletV5R1.from_mnemonic(
                self.tonapi, user.wallet_mnemonic
            )
            return wallet

        wallet, public_key, private_key, mnemonic = WalletV5R1.create(self.tonapi)
        await self.update(
            user,
            wallet_address=wallet.address.to_str(),
            wallet_mnemonic=mnemonic,
        )

        return wallet

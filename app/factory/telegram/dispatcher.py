from __future__ import annotations

from aiogram import Dispatcher, F
from aiogram.enums import ChatType
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from tonutils.client import TonapiClient

from app.factory.redis import create_redis
from app.factory.session_pool import create_session_pool
from app.factory.telegram.i18n import setup_i18n_middleware
from app.models.config import AppConfig
from app.services.database import RedisRepository
from app.services.user import UserService
from app.telegram.handlers import admin, extra, menu, trade, wallet
from app.telegram.middlewares import (
    MessageHelperMiddleware,
    UserMiddleware,
)
from app.utils import mjson


def create_dispatcher(config: AppConfig) -> Dispatcher:
    redis: Redis = create_redis(url=config.redis.build_url())
    session_pool: async_sessionmaker[AsyncSession] = create_session_pool(config=config)
    redis_repository: RedisRepository = RedisRepository(client=redis)
    tonapi: TonapiClient = TonapiClient(api_key=config.common.tonconsole_key.get_secret_value())

    # noinspection PyArgumentList
    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=RedisStorage(
            redis=redis,
            json_loads=mjson.decode,
            json_dumps=mjson.encode,
        ),
        config=config,
        session_pool=session_pool,
        redis=redis_repository,
        user_service=UserService(
            session_pool=session_pool,
            redis=redis_repository,
            config=config,
            tonapi=tonapi,
        ),
        tonapi=tonapi,
    )

    dispatcher.include_routers(
        admin.router,
        menu.router,
        wallet.router,
        extra.router,
        trade.router,
    )
    dispatcher.message.filter(F.chat.type == ChatType.PRIVATE)
    dispatcher.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)

    UserMiddleware().setup_inner(router=dispatcher)
    setup_i18n_middleware(dispatcher=dispatcher, config=config)
    MessageHelperMiddleware().setup_inner(router=dispatcher)
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    return dispatcher

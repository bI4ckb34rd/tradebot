from __future__ import annotations

from aiogram import Dispatcher, F
from aiogram.enums import ChatType
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram_i18n import I18nMiddleware
from coinmarketcapapi import CoinMarketCapAPI
from redis.asyncio import Redis
from tonutils.client import TonapiClient

from app.models.config import AppConfig
from app.services.database.redis import RedisRepository
from app.telegram.handlers import admin, common, extra
from app.telegram.middlewares import MessageHelperMiddleware, UserMiddleware
from app.utils import mjson

from ..redis import create_redis
from ..session_pool import create_session_pool
from .i18n import create_i18n_middleware


def create_dispatcher(config: AppConfig) -> Dispatcher:
    """
    :return: Configured ``Dispatcher`` with installed middlewares and included routers
    """
    redis: Redis = create_redis(url=config.redis.build_url())
    i18n_middleware: I18nMiddleware = create_i18n_middleware(config)

    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=RedisStorage(
            redis=redis,
            json_loads=mjson.decode,
            json_dumps=mjson.encode,
        ),
        config=config,
        session_pool=create_session_pool(config=config),
        redis=RedisRepository(client=redis),
        tonapi=TonapiClient(api_key=config.common.tonconsole_key.get_secret_value()),
        coinmarketcap=CoinMarketCapAPI(api_key=config.common.coinmarketcap_key.get_secret_value()),
    )

    dispatcher.include_routers(admin.router, common.router, extra.router)
    dispatcher.message.filter(F.chat.type == ChatType.PRIVATE)
    dispatcher.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)
    UserMiddleware().setup_inner(router=dispatcher)
    i18n_middleware.setup(dispatcher=dispatcher)
    MessageHelperMiddleware().setup_inner(router=dispatcher)
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    return dispatcher

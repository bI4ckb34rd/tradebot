from typing import Final

from aiogram import Router

from . import buy, copy_trade, limit_orders, sell, token_info, tp_sl_orders

router: Final[Router] = Router(name=__name__)
router.include_routers(
    buy.router,
    copy_trade.router,
    limit_orders.router,
    sell.router,
    token_info.router,
    tp_sl_orders.router,
)

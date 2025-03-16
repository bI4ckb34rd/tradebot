from typing import Final

from aiogram import Router

from . import balance, deposite, withdraw

router: Final[Router] = Router(name=__name__)
router.include_routers(
    balance.router,
    deposite.router,
    withdraw.router,
)

from typing import Final

from aiogram import Router

from . import backup, balance, deposite, setup, unlink, withdraw

router: Final[Router] = Router(name=__name__)
router.include_routers(
    balance.router,
    deposite.router,
    withdraw.router,
    backup.router,
    setup.router,
    unlink.router,
)

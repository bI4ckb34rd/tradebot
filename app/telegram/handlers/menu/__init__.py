from typing import Final

from aiogram import Router

from . import language, main

router: Final[Router] = Router(name=__name__)
router.include_routers(
    main.router,
    language.router,
)

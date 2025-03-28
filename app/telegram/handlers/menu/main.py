from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from aiogram_i18n import I18nContext

from app.telegram.keyboards.callback_data.menu import CDMenu
from app.telegram.keyboards.menu import menu_keyboard
from app.telegram.keyboards.wallet import wallet_setup_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
@router.callback_query(CDMenu.filter())
async def show_main_menu(
    _: TelegramObject,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
    user: UserDto,
) -> Any:
    await state.clear()
    if user.wallet_connected:
        return await helper.answer(
            text=i18n.messages.start(name=user.mention),
            reply_markup=menu_keyboard(i18n=i18n),
        )
    return await helper.answer(
        text=i18n.messages.wallet.setup(),
        reply_markup=wallet_setup_keyboard(i18n=i18n),
    )

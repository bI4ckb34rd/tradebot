from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router, flags
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, TelegramObject
from aiogram_i18n import I18nContext

from app.telegram.keyboards.callback_data.menu import (
    CDCopyTrade,
    CDLimitOrder,
    CDMenu,
    CDTpSlOrders,
)
from app.telegram.keyboards.menu import main_keyboard

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
    return await helper.answer(
        text=i18n.messages.start(name=user.mention),
        reply_markup=main_keyboard(i18n=i18n),
    )


@router.callback_query(CDTpSlOrders.filter())
@router.callback_query(CDLimitOrder.filter())
@router.callback_query(CDCopyTrade.filter())
@flags.callback_answer(disabled=True)
async def answer_soon(query: CallbackQuery, i18n: I18nContext) -> Any:
    return query.answer(text=i18n.messages.soon(_path="menu.ftl"))

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from app.telegram.filters.states import SGUnlinkWallet
from app.telegram.keyboards.callback_data.trade import CDConfirm
from app.telegram.keyboards.callback_data.wallet import CDUnlinkWallet
from app.telegram.keyboards.menu import confirm_keyboard, to_menu_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.services.user import UserService
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDUnlinkWallet.filter())
@flags.callback_answer(disabled=True)
async def unlink_wallet(
    _: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.set_state(SGUnlinkWallet.confirm)
    message: Message = await helper.answer(  # type: ignore[assignment]
        text=i18n.messages.wallet.unlink_confirm(),
        reply_markup=confirm_keyboard(i18n=i18n),
    )
    await state.set_data({"message_id": message.message_id})


@router.callback_query(SGUnlinkWallet.confirm, CDConfirm.filter())
async def process_unlink_wallet(
    _: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
    user: UserDto,
    user_service: UserService,
) -> Any:
    await user_service.update(
        user,
        wallet_address=None,
        wallet_mnemonic=None,
    )
    await state.clear()
    return await helper.answer(
        text=i18n.messages.wallet.unlinked(),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

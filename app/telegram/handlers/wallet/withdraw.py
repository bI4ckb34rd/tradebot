from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import F, Router, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from tonutils.wallet import WalletV5R1

from app.telegram.filters.states import SGWithdraw
from app.telegram.keyboards.callback_data.trade import CDConfirm
from app.telegram.keyboards.callback_data.wallet import CDWithdraw
from app.telegram.keyboards.menu import confirm_keyboard, to_menu_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.services.user import UserService
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDWithdraw.filter())
@flags.callback_answer(disabled=True)
async def withdraw_balance(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.set_state(SGWithdraw.enter_address)
    message: Message = await helper.answer(  # type: ignore[assignment]
        text=i18n.messages.withdraw.ask_address(),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )
    await state.set_data({"message_id": message.message_id})


@router.message(SGWithdraw.enter_address, F.text.as_("address"))
async def enter_amount(
    _: Message,
    helper: MessageHelper,
    address: str,
    i18n: I18nContext,
) -> Any:
    await helper.next_step(
        state=SGWithdraw.enter_amount,
        text=i18n.messages.withdraw.ask_amount(),
        reply_markup=to_menu_keyboard(i18n=i18n),
        update={"address": address.lower()},
    )


@router.message(SGWithdraw.enter_amount, F.text.cast(int).as_("amount"))
async def enter_destination(
    _: Message,
    helper: MessageHelper,
    amount: int,
    i18n: I18nContext,
) -> Any:
    await helper.next_step(
        state=SGWithdraw.enter_destination,
        text=i18n.messages.withdraw.ask_destination(),
        reply_markup=to_menu_keyboard(i18n=i18n),
        update={"amount": amount},
    )


@router.message(SGWithdraw.enter_destination, F.text.as_("destination"))
async def confirm_withdrawal(
    _: Message,
    helper: MessageHelper,
    state: FSMContext,
    destination: str,
    i18n: I18nContext,
) -> Any:
    data: dict[str, Any] = await state.get_data()
    token_type = "ton" if data["address"] == "ton" else "other"

    await helper.next_step(
        state=SGWithdraw.confirm,
        text=i18n.messages.withdraw.confirm(
            address=data["address"],
            amount=data["amount"],
            token_type=token_type,
            destination=destination,
        ),
        reply_markup=confirm_keyboard(i18n=i18n),
        update={"destination": destination},
    )


@router.callback_query(SGWithdraw.confirm, CDConfirm.filter())
async def process_withdrawal(
    _: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
    user: UserDto,
    user_service: UserService,
) -> Any:
    data: dict[str, Any] = await state.get_data()
    wallet: WalletV5R1 = await user_service.get_wallet(user)

    try:
        if data["address"] == "ton":
            tx_hash = await wallet.transfer(
                destination=data["destination"],
                amount=data["amount"],
            )
        else:
            tx_hash = await wallet.transfer_jetton(
                destination=data["destination"],
                jetton_master_address=data["address"],
                jetton_amount=data["amount"],
            )
        text = i18n.messages.withdraw.result(tx_hash=tx_hash)
    except:
        text = i18n.messages.something_went_wrong(_path="errors.ftl")
    await state.clear()
    await helper.answer(
        text=text,
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from tonutils.wallet import WalletV5R1

from app.telegram.filters.states import SGBuy
from app.telegram.keyboards.callback_data.trade import CDBuy, CDConfirm
from app.telegram.keyboards.menu import confirm_keyboard, to_menu_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.services.user import UserService
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDBuy.filter())
async def proceed_buy(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.set_state(SGBuy.enter_address)
    message: Message = await helper.answer(  # type: ignore[assignment]
        text=i18n.messages.buy.ask_address(),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )
    await state.set_data({"message_id": message.message_id})


@router.message(SGBuy.enter_address, F.text.as_("address"))
async def enter_amount(
    _: Message,
    helper: MessageHelper,
    address: str,
    i18n: I18nContext,
) -> Any:
    await helper.next_step(
        state=SGBuy.enter_amount,
        text=i18n.messages.buy.ask_amount(),
        reply_markup=to_menu_keyboard(i18n=i18n),
        update={"address": address},
    )


@router.message(SGBuy.enter_amount, F.text.cast(int).as_("amount"))
async def confirm_purchase(
    _: Message,
    helper: MessageHelper,
    state: FSMContext,
    amount: int,
    i18n: I18nContext,
) -> Any:
    data: dict[str, Any] = await state.get_data()

    await helper.next_step(
        state=SGBuy.confirm,
        text=i18n.messages.buy.confirm(
            address=data["address"],
            amount=amount,
        ),
        reply_markup=confirm_keyboard(i18n=i18n),
        update={"amount": amount},
    )


@router.callback_query(SGBuy.confirm, CDConfirm.filter())
async def buy_token(
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
        tx_hash = await wallet.dedust_swap_ton_to_jetton(
            jetton_master_address=data["address"],
            ton_amount=data["amount"],
        )
        text = i18n.messages.buy.result(tx_hash=tx_hash)
    except:
        text = i18n.messages.something_went_wrong()
    await state.clear()
    await helper.answer(
        text=text,
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

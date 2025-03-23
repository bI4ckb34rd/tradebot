from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import F, Router, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from tonutils.wallet import WalletV5R1

from app.telegram.filters.states import SGImportWallet
from app.telegram.keyboards.callback_data.wallet import CDCreateWallet, CDImportWallet
from app.telegram.keyboards.menu import to_menu_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.services.user import UserService
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDCreateWallet.filter())
@flags.callback_answer(disabled=True)
async def create_wallet(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    user: UserDto,
    user_service: UserService,
) -> Any:
    wallet, public_key, private_key, mnemonic = WalletV5R1.create(user_service.tonapi)
    await user_service.update(
        user,
        wallet_address=wallet.address.to_str(),
        wallet_mnemonic=mnemonic,
    )
    return await helper.answer(
        text=i18n.messages.wallet.created(
            address=wallet.address.to_str(),
            mnemonic=" ".join(mnemonic),
        ),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )


@router.callback_query(CDImportWallet.filter())
@flags.callback_answer(disabled=True)
async def import_wallet(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.set_state(SGImportWallet.enter_mnemonic)
    message: Message = await helper.answer(  # type: ignore[assignment]
        text=i18n.messages.wallet.import_ask(),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )
    await state.set_data({"message_id": message.message_id})


@router.message(SGImportWallet.enter_mnemonic, F.text.as_("mnemonic"))
async def process_import(
    _: Message,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
    mnemonic: str,
    user: UserDto,
    user_service: UserService,
) -> Any:
    try:
        words = mnemonic.split()
        if len(words) != 24:
            raise ValueError("Invalid mnemonic length")

        wallet, public_key, private_key, mnemonic = WalletV5R1.from_mnemonic(
            user_service.tonapi, words
        )
        await user_service.update(
            user,
            wallet_address=wallet.address.to_str(),
            wallet_mnemonic=mnemonic,
        )
        text = i18n.messages.wallet.import_success(
            address=wallet.address.to_str(),
        )
    except Exception:
        text = i18n.messages.wallet.import_error()

    await state.clear()
    return await helper.answer(
        text=text,
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

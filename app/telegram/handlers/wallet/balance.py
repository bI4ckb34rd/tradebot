from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router
from aiogram.types import TelegramObject
from aiogram_i18n import I18nContext
from aiohttp import ClientResponseError
from tonutils.utils import to_amount

from app.telegram.keyboards.callback_data.wallet import CDWallet
from app.telegram.keyboards.wallet import wallet_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.services.user import UserService
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDWallet.filter())
async def handle_wallet(
    _: TelegramObject,
    helper: MessageHelper,
    i18n: I18nContext,
    user: UserDto,
    user_service: UserService,
) -> Any:
    wallet = await user_service.get_wallet(user)

    try:
        ton_balance = await wallet.balance()
        ton_balance = to_amount(ton_balance)
    except ClientResponseError:
        ton_balance = 0

    return await helper.answer(
        text=i18n.messages.wallet_info(
            address=wallet.address.to_str(),
            ton_balance=ton_balance,
        ),
        reply_markup=wallet_keyboard(i18n=i18n),
    )

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router, flags
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from app.telegram.keyboards.callback_data.wallet import CDBackup
from app.telegram.keyboards.menu import to_menu_keyboard

if TYPE_CHECKING:
    from app.models.dto import UserDto
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDBackup.filter())
@flags.callback_answer(disabled=True)
async def show_backup(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    user: UserDto,
) -> Any:
    return await helper.answer(
        text=i18n.messages.backup.warning(
            mnemonic=" ".join(user.wallet_mnemonic),
        ),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

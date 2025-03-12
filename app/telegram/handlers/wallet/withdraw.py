from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import Router, flags
from aiogram.types import CallbackQuery
from aiogram_i18n import I18nContext

from app.telegram.keyboards.callback_data.wallet import CDWithdraw

if TYPE_CHECKING:
    pass

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDWithdraw.filter())
@flags.callback_answer(disabled=True)
async def withdraw_balance(query: CallbackQuery, i18n: I18nContext) -> Any:
    return query.answer(text=i18n.messages.soon())

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from .callback_data.menu import CDMenu
from .callback_data.wallet import CDDeposit, CDWithdraw


def wallet_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.deposite(), callback_data=CDDeposit())
    builder.button(text=i18n.buttons.withdraw(), callback_data=CDWithdraw())
    builder.button(text=i18n.buttons.back(), callback_data=CDMenu())
    builder.adjust(2, 1)
    return builder.as_markup()

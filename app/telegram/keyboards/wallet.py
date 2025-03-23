from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from .callback_data.menu import CDMenu
from .callback_data.wallet import (
    CDBackup,
    CDCreateWallet,
    CDDeposit,
    CDImportWallet,
    CDUnlinkWallet,
    CDWithdraw,
)


def wallet_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.deposite(), callback_data=CDDeposit())
    builder.button(text=i18n.buttons.withdraw(), callback_data=CDWithdraw())
    builder.button(text=i18n.buttons.backup(), callback_data=CDBackup())
    builder.button(text=i18n.buttons.unlink_wallet(), callback_data=CDUnlinkWallet())
    builder.button(text=i18n.buttons.back(), callback_data=CDMenu())
    builder.adjust(2, 2, 1)
    return builder.as_markup()


def wallet_setup_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.create_wallet(), callback_data=CDCreateWallet())
    builder.button(text=i18n.buttons.import_wallet(), callback_data=CDImportWallet())
    builder.adjust(1)
    return builder.as_markup()

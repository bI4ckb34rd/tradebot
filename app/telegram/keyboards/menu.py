from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from .callback_data.menu import (
    CDLanguage,
    CDMenu,
)
from .callback_data.trade import (
    CDBuy,
    CDConfirm,
    CDCopyTrade,
    CDLimitOrder,
    CDSell,
    CDTokenInfo,
    CDTpSlOrders,
)
from .callback_data.wallet import CDWallet


def to_menu_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.menu(), callback_data=CDMenu())
    return builder.as_markup()


def cancel_keyboard(i18n: I18nContext, data: CallbackData) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.cancel(), callback_data=data)
    return builder.as_markup()


def back_keyboard(i18n: I18nContext, data: CallbackData) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.back(), callback_data=data)
    return builder.as_markup()


def menu_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.wallet(), callback_data=CDWallet())
    builder.button(text=i18n.buttons.buy(), callback_data=CDBuy())
    builder.button(text=i18n.buttons.sell(), callback_data=CDSell())
    builder.button(text=i18n.buttons.token_info(), callback_data=CDTokenInfo())
    builder.button(text=i18n.buttons.tp_sl_orders(), callback_data=CDTpSlOrders())
    builder.button(text=i18n.buttons.limit_order(), callback_data=CDLimitOrder())
    builder.button(text=i18n.buttons.copy_trade(), callback_data=CDCopyTrade())
    builder.button(text=i18n.buttons.language(), callback_data=CDLanguage())
    builder.adjust(1, 2, 2, 2, 1)
    return builder.as_markup()


def confirm_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.confirm(), callback_data=CDConfirm())
    builder.button(text=i18n.buttons.cancel(), callback_data=CDMenu())
    return builder.as_markup()

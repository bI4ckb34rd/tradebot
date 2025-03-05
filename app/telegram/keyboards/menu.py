from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext

from .callback_data.menu import (
    CDBuy,
    CDCopyTrade,
    CDDeposit,
    CDLimitOrder,
    CDMenu,
    CDSell,
    CDTokenInfo,
    CDTpSlOrders,
    CDWallet,
    CDWithdraw,
)


def main_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.wallet(_path="menu.ftl"), callback_data=CDWallet())
    builder.button(text=i18n.buttons.buy(_path="menu.ftl"), callback_data=CDBuy())
    builder.button(text=i18n.buttons.sell(_path="menu.ftl"), callback_data=CDSell())
    builder.button(text=i18n.buttons.token_info(_path="menu.ftl"), callback_data=CDTokenInfo())
    builder.button(text=i18n.buttons.tp_sl_orders(_path="menu.ftl"), callback_data=CDTpSlOrders())
    builder.button(text=i18n.buttons.limit_order(_path="menu.ftl"), callback_data=CDLimitOrder())
    builder.button(text=i18n.buttons.copy_trade(_path="menu.ftl"), callback_data=CDCopyTrade())
    builder.adjust(1, 2, 2, 2)
    return builder.as_markup()

def wallet_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.deposite(_path="menu.ftl"), callback_data=CDDeposit())
    builder.button(text=i18n.buttons.withdraw(_path="menu.ftl"), callback_data=CDWithdraw())
    builder.button(text=i18n.buttons.back(_path="menu.ftl"), callback_data=CDMenu())
    builder.adjust(2, 1)
    return builder.as_markup()


def cancel_keyboard(i18n: I18nContext, data: CallbackData) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.cancel(_path="menu.ftl"), callback_data=data)
    return builder.as_markup()


def back_keyboard(i18n: I18nContext) -> InlineKeyboardMarkup:
    builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    builder.button(text=i18n.buttons.back(_path="menu.ftl"), callback_data=CDMenu())
    return builder.as_markup()

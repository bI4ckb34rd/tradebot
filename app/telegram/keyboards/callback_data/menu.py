from aiogram.filters.callback_data import CallbackData


class CDMenu(CallbackData, prefix="menu"):
    pass


class CDWallet(CallbackData, prefix="wallet"):
    pass


class CDBuy(CallbackData, prefix="buy"):
    pass


class CDSell(CallbackData, prefix="sell"):
    pass


class CDTokenInfo(CallbackData, prefix="token_info"):
    pass


class CDTpSlOrders(CallbackData, prefix="tp_sl_orders"):
    pass


class CDLimitOrder(CallbackData, prefix="limit_order"):
    pass


class CDCopyTrade(CallbackData, prefix="copy_trade"):
    pass


class CDDeposit(CallbackData, prefix="deposit"):
    pass


class CDWithdraw(CallbackData, prefix="withdraw"):
    pass

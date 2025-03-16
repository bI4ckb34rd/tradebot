from aiogram.filters.callback_data import CallbackData


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

class CDConfirm(CallbackData, prefix="confirm"):
    pass

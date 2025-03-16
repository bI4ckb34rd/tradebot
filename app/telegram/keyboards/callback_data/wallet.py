from aiogram.filters.callback_data import CallbackData


class CDWallet(CallbackData, prefix="wallet"):
    pass


class CDDeposit(CallbackData, prefix="deposit"):
    pass


class CDWithdraw(CallbackData, prefix="withdraw"):
    pass

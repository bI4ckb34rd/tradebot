from aiogram.filters.callback_data import CallbackData


class CDWallet(CallbackData, prefix="wallet"):
    pass


class CDDeposit(CallbackData, prefix="deposit"):
    pass


class CDWithdraw(CallbackData, prefix="withdraw"):
    pass


class CDBackup(CallbackData, prefix="backup"):
    pass


class CDCreateWallet(CallbackData, prefix="create_wallet"):
    pass


class CDImportWallet(CallbackData, prefix="import_wallet"):
    pass


class CDUnlinkWallet(CallbackData, prefix="unlink_wallet"):
    pass

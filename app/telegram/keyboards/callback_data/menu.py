from aiogram.filters.callback_data import CallbackData


class CDMenu(CallbackData, prefix="menu"):
    pass


class CDLanguage(CallbackData, prefix="language"):
    pass


class CDSetLanguage(CallbackData, prefix="set_language"):
    locale: str

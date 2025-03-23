from typing import Final

from aiogram.filters import Filter, StateFilter
from aiogram.fsm.state import State, StatesGroup

NoneState: Final[Filter] = StateFilter(None)
AnyState: Final[Filter] = ~NoneState


class SGTokenInfo(StatesGroup):
    token_symbol = State()


class SGBuy(StatesGroup):
    enter_address = State()
    enter_amount = State()
    # select_currency = State()
    confirm = State()


class SGSell(StatesGroup):
    enter_address = State()
    enter_amount = State()
    # select_currency = State()
    confirm = State()


class SGWithdraw(StatesGroup):
    enter_address = State()
    enter_amount = State()
    enter_destination = State()
    confirm = State()


class SGImportWallet(StatesGroup):
    enter_mnemonic = State()


class SGUnlinkWallet(StatesGroup):
    confirm = State()

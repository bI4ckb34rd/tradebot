from pytoniq_core import Address, AddressError
from swapcoffee.tokens import SwapCoffee
from swapcoffee.tokens.types import BlockchainToken


class TokenPriceService:
    def __init__(self):
        self.coffee = SwapCoffee()

    async def get_token_price(self, user_input: str) -> BlockchainToken | None:
        try:
            if self.is_address(user_input):
                return await self.coffee.get_token_by_address(address=user_input)
            else:
                tokens = await self.coffee.get_tokens_by_symbols(symbols=[user_input.upper()])
                if tokens:
                    return tokens[0]
            return None
        except Exception:
            return None

    async def close(self):
        await self.coffee.session.close()

    @staticmethod
    def is_address(value: str) -> bool:
        """Checks if the given address is a valid ton blockchain address."""
        try:
            _ = Address(value)
            return True
        except AddressError:
            return False

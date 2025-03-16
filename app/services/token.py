from typing import Optional

from swapcoffee.tokens import SwapCoffee
from swapcoffee.tokens.types import BlockchainToken


class TokenService:
    def __init__(self):
        self.coffee = SwapCoffee()

    async def get_token_by_symbol(self, symbol: str) -> Optional[BlockchainToken]:
        """Get a single token by symbol"""
        tokens = await self.coffee.get_tokens_by_symbols(symbols=[symbol])
        return tokens[0] if tokens else None

    async def get_token_by_address(self, address: str) -> Optional[BlockchainToken]:
        """Get a token by its contract address"""
        # Depending on the API capabilities, implement address lookup
        # This is just a placeholder - check the actual method in the package
        tokens = await self.coffee.get_tokens_by_addresses(addresses=[address])
        return tokens[0] if tokens else None

    async def close(self):
        """Close the underlying session"""
        if self.coffee and self.coffee.session:
            await self.coffee.session.close()

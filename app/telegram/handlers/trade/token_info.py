from __future__ import annotations

from typing import TYPE_CHECKING, Any, Final

from aiogram import F, Router, flags
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext

from app.services.token_price import TokenPriceService
from app.telegram.filters.states import SGTokenInfo
from app.telegram.keyboards.callback_data.trade import CDTokenInfo
from app.telegram.keyboards.menu import to_menu_keyboard
from app.utils.ton import convert_address

if TYPE_CHECKING:
    from app.telegram.helpers.messages import MessageHelper

router: Final[Router] = Router(name=__name__)


@router.callback_query(CDTokenInfo.filter())
@flags.callback_answer(disabled=True)
async def proceed_token_info(
    query: CallbackQuery,
    helper: MessageHelper,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.set_state(SGTokenInfo.token_symbol)
    message: Message = await helper.answer(  # type: ignore[assignment]
        text=i18n.messages.ask_symbol(),
        reply_markup=to_menu_keyboard(i18n=i18n),
    )
    await state.set_data({"message_id": message.message_id})


@router.message(SGTokenInfo.token_symbol, F.text.as_("symbol"))
async def process_token_symbol(
    _: Message,
    helper: MessageHelper,
    symbol: str,
    i18n: I18nContext,
    state: FSMContext,
) -> Any:
    await state.clear()
    token_service = TokenPriceService()
    try:
        token = await token_service.get_token_price(symbol)
        if token:
            response_text = i18n.messages.token_info(
                name=token.name,
                symbol=token.symbol,
                price=token.price_usd,
                price_change=token.price_change_24h,
                tvl=token.tvl,
                holders=token.holders_count,
                trust_score=token.trust_score,
                address=convert_address(token.address),
            )
        else:
            response_text = i18n.messages.token_not_found(symbol=symbol)
    except Exception:
        response_text = i18n.messages.token_error()
    finally:
        await token_service.close()
    await helper.answer(
        text=response_text,
        reply_markup=to_menu_keyboard(i18n=i18n),
    )

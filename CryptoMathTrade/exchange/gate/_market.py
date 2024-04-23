import time

from ._api import API
from .core import MarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 10) -> Response:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 10; max 5000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self, symbol: str, limit: int = 100) -> Response:
        """Recent Trades List

        GET /api/v4/spot/trades

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return Response(data=[Trade(id=trade.get('id'),
                                    price=trade.get('price'),
                                    quantity=trade.get('amount'),
                                    side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                    time=trade.get('create_time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v4/spot/tickers

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()
        return Response(data=[Ticker(symbol=ticker.get('currency_pair'),
                                     openPrice=float(ticker.get('last')) / (
                                             1 + float(ticker.get('change_percentage')) / 100),
                                     highPrice=ticker.get('high_24h'),
                                     lowPrice=ticker.get('low_24h'),
                                     lastPrice=ticker.get('last'),
                                     volume=ticker.get('base_volume'),
                                     quoteVolume=ticker.get('quote_volume'),
                                     closeTime=int(time.time()),
                                     ) for ticker in json_data], response_object=response)

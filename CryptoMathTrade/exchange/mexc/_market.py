from ._api import API
from .core import MarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100) -> Response:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self, symbol: str, limit: int = 500) -> Response:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()
        return Response(data=[Trade(id=trade.get('id'),
                                    price=trade.get('price'),
                                    quantity=trade.get('qty'),
                                    side=Side.SELL if trade.get('isBuyerMaker') else Side.BUY,
                                    time=trade.get('time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()

        if isinstance(json_data, list):
            data = [Ticker(**ticker) for ticker in json_data]
        elif isinstance(json_data, dict):
            data = [Ticker(**json_data)]
        else:
            raise Exception(json_data)

        return Response(data=data, response_object=response)


class AsyncMarket(API):
    async def get_depth(self, symbol: str, limit: int = 100) -> Response:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    async def get_trades(self, symbol: str, limit: int = 500) -> Response:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json
        return Response(data=[Trade(id=trade.get('id'),
                                    price=trade.get('price'),
                                    quantity=trade.get('qty'),
                                    side=Side.SELL if trade.get('isBuyerMaker') else Side.BUY,
                                    time=trade.get('time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    async def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json

        if isinstance(json_data, list):
            data = [Ticker(**ticker) for ticker in json_data]
        elif isinstance(json_data, dict):
            data = [Ticker(**json_data)]
        else:
            raise Exception(json_data)

        return Response(data=data, response_object=response)

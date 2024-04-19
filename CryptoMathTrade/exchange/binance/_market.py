from typing import Generator

from ._api import API
from .core import MarketCore, WSMarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response, validate_async_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 100) -> Response:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        params:
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

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

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

    def get_ticker(self, symbol: str | None = None, symbols: list | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair

            symbols (list, optional): list of trading pairs
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol, symbols=symbols)))
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

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        response = validate_async_response(
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

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        response = validate_async_response(
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

    async def get_ticker(self, symbol: str | None = None, symbols: list | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair

            symbols (list, optional): list of trading pairs
        """
        response = validate_async_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol, symbols=symbols)))
        json_data = response.json

        if isinstance(json_data, list):
            data = [Ticker(**ticker) for ticker in json_data]
        elif isinstance(json_data, dict):
            data = [Ticker(**json_data)]
        else:
            raise Exception(json_data)

        return Response(data=data,
                        response_object=response,
                        )


#  TODO: Socket
class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ) -> Generator:
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        param:
            symbol (str): the trading pair

        Update Speed: 1000ms or 100ms
        """
        return self._ws_query(**WSMarketCore(headers=self.headers).get_depth_args(symbol=symbol))

    async def get_trades(self,
                         symbol: str,
                         ) -> Generator:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.

         Stream Name: <symbol>@trade

         param:
            symbol (str): the trading pair

         Update Speed: Real-time
         """
        return self._ws_query(**WSMarketCore(headers=self.headers).get_trades_args(symbol=symbol))

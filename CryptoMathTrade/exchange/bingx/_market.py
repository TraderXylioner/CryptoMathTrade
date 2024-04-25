from typing import Generator

from ._api import API
from .core import MarketCore, WSMarketCore
from .._response import Response
from ..utils import validate_response
from ...types import OrderBook, Trade, Ticker, Order


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int = 100,
                  recvWindow: int | None = None,
                  ) -> Response:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000

            recvWindow (int, optional).
        """
        response = validate_response(self._query(
            **MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow)))
        json_data = response.json()['data']
        json_data['asks'] = json_data['asks'][::-1]
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self,
                   symbol: str,
                   limit: int = 100,
                   recvWindow: int | None = None,
                   ) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 100

            recvWindow (int, optional).
        """
        response = validate_response(self._query(
            **MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit, recvWindow=recvWindow)))
        json_data = response.json()['data']
        return Response(data=[Trade(id=trade.get('id'),
                                    price=trade.get('price'),
                                    quantity=trade.get('qty'),
                                    time=trade.get('time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self,
                   symbol: str | None = None
                   ):
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                     priceChange=ticker.get('priceChange'),
                                     priceChangePercent=ticker.get('priceChangePercent')[:-1],
                                     openPrice=ticker.get('openPrice'),
                                     highPrice=ticker.get('highPrice'),
                                     lowPrice=ticker.get('lowPrice'),
                                     lastPrice=ticker.get('lastPrice'),
                                     volume=ticker.get('volume'),
                                     quoteVolume=ticker.get('quoteVolume'),
                                     openTime=ticker.get('openTime'),
                                     closeTime=ticker.get('closeTime'),
                                     ) for ticker in json_data],
                        response_object=response,
                        )


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int = 100,
                        recvWindow: int | None = None
                        ):
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 1000. If limit > 1000, then the response will truncate to 1000

            recvWindow (int, optional).
        """
        response = validate_response(await self._async_query(
            **MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, recvWindow=recvWindow)))
        json_data = response.json['data']
        json_data['asks'] = json_data['asks'][::-1]
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    async def get_trades(self,
                         symbol: str,
                         limit: int = 100):
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 100
        """
        response = validate_response(await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return Response(data=[Trade(id=trade.get('id'),
                                    price=trade.get('price'),
                                    quantity=trade.get('qty'),
                                    time=trade.get('time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    async def get_ticker(self,
                         symbol: str | None = None
                         ):
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        response = validate_response(await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json['data']
        return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                     priceChange=ticker.get('priceChange'),
                                     priceChangePercent=ticker.get('priceChangePercent')[:-1],
                                     openPrice=ticker.get('openPrice'),
                                     highPrice=ticker.get('highPrice'),
                                     lowPrice=ticker.get('lowPrice'),
                                     lastPrice=ticker.get('lastPrice'),
                                     volume=ticker.get('volume'),
                                     quoteVolume=ticker.get('quoteVolume'),
                                     openTime=ticker.get('openTime'),
                                     closeTime=ticker.get('closeTime'),
                                     ) for ticker in json_data],
                        response_object=response,
                        )


class WebsSocketMarket(API):
    async def get_depth(self,
                        symbol: str,
                        ) -> Generator:
        """Partial Book Depth Streams

        Top bids and asks.

        Stream Names: <symbol>@depth<levels>.

        param:
            symbol (str): the trading pair
        """
        return self._ws_query(**ws_get_depth_args(symbol=symbol))

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
        return self._ws_query(**ws_get_trades_args(symbol=symbol))

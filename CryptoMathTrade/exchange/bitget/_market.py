from ._api import API
from .core import MarketCore
from CryptoMathTrade.types import OrderBook, Trade, Ticker, Order
from ..utils import validate_response, validate_async_response
from .._response import Response


class Market(API):
    def get_depth(self,
                  symbol: str,
                  limit: int = 150,
                  ) -> Response:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self,
                   symbol: str,
                   limit: int = 100,
                   ) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return Response(data=[Trade(id=trade.get('tradeId'),
                                    price=trade.get('price'),
                                    quantity=trade.get('size'),
                                    time=trade.get('ts'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self,
                   symbol: str | None = None,
                   ) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                     priceChange=float(ticker['open']) - float(ticker['lastPr']),
                                     priceChangePercent=((float(ticker['open']) - float(ticker['lastPr'])) / (float(ticker['open'] if float(ticker['open']) else 1))) * 100,
                                     openPrice=ticker.get('open'),
                                     highPrice=ticker.get('high24h'),
                                     lowPrice=ticker.get('low24h'),
                                     lastPrice=ticker.get('lastPr'),
                                     volume=ticker.get('baseVolume'),
                                     quoteVolume=ticker.get('quoteVolume'),
                                     # openTime=ticker.get('openTime'),
                                     closeTime=ticker.get('ts'),
                                     ) for ticker in json_data],
                        response_object=response,
                        )


class AsyncMarket(API):
    async def get_depth(self,
                        symbol: str,
                        limit: int = 100,
                        ) -> Response:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 150; max 150.

            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        response = validate_async_response(
            await self._async_query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    async def get_trades(self,
                         symbol: str,
                         limit: int = 100,
                         ) -> Response:
        """Recent Trades List
        Get recent trades (up to last 100).

        GET /api/v2/spot/market/fills

        https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 500.
        """
        response = validate_async_response(
            await self._async_query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json['data']
        return Response(data=[Trade(id=trade.get('tradeId'),
                                    price=trade.get('price'),
                                    quantity=trade.get('size'),
                                    time=trade.get('ts'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    async def get_ticker(self,
                         symbol: str | None = None,
                         ) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v2/spot/market/tickers

        https://www.bitget.com/api-doc/spot/market/Get-Tickers

        params:
            symbol (str, optional): the trading pair
        """
        response = validate_async_response(
            await self._async_query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json['data']
        return Response(data=[Ticker(symbol=ticker.get('symbol'),
                                     priceChange=float(ticker['open']) - float(ticker['lastPr']),
                                     priceChangePercent=((float(ticker['open']) - float(ticker['lastPr'])) / (float(ticker['open'] if float(ticker['open']) else 1))) * 100,
                                     openPrice=ticker.get('open'),
                                     highPrice=ticker.get('high24h'),
                                     lowPrice=ticker.get('low24h'),
                                     lastPrice=ticker.get('lastPr'),
                                     volume=ticker.get('baseVolume'),
                                     quoteVolume=ticker.get('quoteVolume'),
                                     # openTime=ticker.get('openTime'),
                                     closeTime=ticker.get('ts'),
                                     ) for ticker in json_data],
                        response_object=response,
                        )

from ._api import API
from .core import MarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str) -> Response:
        """Get orderbook.

        GET /api/v1/market/orderbook/level2_100

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-

        param:
            symbol (str): the trading pair

        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol)))
        json_data = response.json()['data']
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self, symbol: str) -> Response:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v1/market/histories

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories

        params:
            symbol (str): the trading pair
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol)))
        json_data = response.json()['data']
        return Response(data=[Trade(id=trade.get('sequence'),
                                    price=trade.get('price'),
                                    quantity=trade.get('size'),
                                    side=Side.BUY if trade.get('side') == 'buy' else Side.SELL,
                                    time=trade.get('time'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /api/v1/market/stats or /api/v1/market/allTickers

        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
        or
        https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        if symbol:
            data = [Ticker(symbol=json_data.get('symbol'),
                           openPrice=float(json_data.get('last')) - float(json_data.get('changePrice')),
                           highPrice=json_data.get('high'),
                           lowPrice=json_data.get('low'),
                           lastPrice=json_data.get('last'),
                           volume=json_data.get('vol'),
                           quoteVolume=json_data.get('volValue'),
                           closeTime=json_data.get('time'),
                           )]
        else:
            full_json_data = json_data
            json_data = json_data['ticker']
            data = [Ticker(symbol=ticker.get('symbol'),
                           openPrice=float(ticker.get('last')) - float(ticker.get('changePrice')),
                           highPrice=ticker.get('high'),
                           lowPrice=ticker.get('low'),
                           lastPrice=ticker.get('last'),
                           volume=ticker.get('vol'),
                           quoteVolume=ticker.get('volValue'),
                           closeTime=full_json_data.get('time'),
                           ) for ticker in json_data]

        return Response(data=data, response_object=response)

from ._api import API
from .core import MarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = 35) -> Response:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 35; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        if 'data' not in json_data:
            raise Exception(json_data)
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self, symbol: str, limit: int = 50) -> Response:
        """Recent Trades List
        Get recent trades (up to last 50).

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 50; max 50.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        if 'data' not in json_data:
            raise Exception(json_data)
        return Response(data=[Trade(price=trade[2],
                                    quantity=trade[3],
                                    side=Side.BUY if trade[4] == 'buy' else Side.SELL,
                                    time=trade[1],
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        json_data = response.json()['data']
        if 'data' not in json_data:
            raise Exception(json_data)

        if isinstance(json_data, list):
            data = [Ticker(symbol=ticker[0],
                           openPrice=ticker[4],
                           highPrice=ticker[5],
                           lowPrice=ticker[6],
                           lastPrice=ticker[1],
                           volume=ticker[2],
                           quoteVolume=ticker[3],
                           closeTime=ticker[12],
                           ) for ticker in json_data]
        elif isinstance(json_data, dict):
            data = [Ticker(symbol=json_data.get('symbol'),
                           openPrice=json_data.get('open_24h'),
                           highPrice=json_data.get('high_24h'),
                           lowPrice=json_data.get('low_24h'),
                           lastPrice=json_data.get('last'),
                           volume=json_data.get('v_24h'),
                           quoteVolume=json_data.get('qv_24h'),
                           closeTime=json_data.get('ts'),
                           )]
        else:
            raise Exception(json_data)

        return Response(data=data, response_object=response)

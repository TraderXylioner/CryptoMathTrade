import time

from ._api import API
from .core import MarketCore
from ...types import OrderBook, Trade, Ticker, Order, Side
from ..utils import validate_response
from .._response import Response


class Market(API):
    def get_depth(self, symbol: str, limit: int = None, type: str = 'step0') -> Response:
        """Get orderbook.

        GET /market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 20 or 150; max 20 or 150.
            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.

            when type is set to "step0", the default value of "depth" is 150 instead of 20.

            step0	No market depth aggregation
            step1	Aggregation level = precision*10
            step2	Aggregation level = precision*100
            step3	Aggregation level = precision*1000
            step4	Aggregation level = precision*10000
            step5	Aggregation level = precision*100000
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_depth_args(symbol=symbol, limit=limit, type=type)))
        json_data = response.json()['tick']
        return Response(data=OrderBook(asks=[Order(price=ask[0], volume=ask[1]) for ask in json_data['asks']],
                                       bids=[Order(price=bid[0], volume=bid[1]) for bid in json_data['bids']],
                                       ),
                        response_object=response,
                        )

    def get_trades(self, symbol: str, limit: int = 1) -> Response:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_trades_args(symbol=symbol, limit=limit)))
        json_data = response.json()['data']
        return Response(data=[Trade(id=trade['data'][0].get('trade-id'),
                                    price=trade['data'][0].get('price'),
                                    quantity=trade['data'][0].get('amount'),
                                    side=Side.BUY if trade['data'][0].get('direction') == 'buy' else Side.SELL,
                                    time=trade['data'][0].get('ts'),
                                    ) for trade in json_data],
                        response_object=response,
                        )

    def get_ticker(self, symbol: str | None = None) -> Response:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        response = validate_response(
            self._query(**MarketCore(headers=self.headers).get_ticker_args(symbol=symbol)))
        full_json_data = response.json()
        json_data = full_json_data['tick'] if symbol else full_json_data['data']

        if isinstance(json_data, list):
            data = [Ticker(symbol=ticker.get('symbol'),
                           openPrice=ticker.get('open'),
                           highPrice=ticker.get('high'),
                           lowPrice=ticker.get('low'),
                           lastPrice=ticker.get('close'),
                           volume=ticker.get('amount'),
                           quoteVolume=ticker.get('vol'),
                           closeTime=full_json_data.get('ts'),
                           ) for ticker in json_data]
        elif isinstance(json_data, dict):
            data = [Ticker(symbol=symbol,
                           openPrice=json_data.get('open'),
                           highPrice=json_data.get('high'),
                           lowPrice=json_data.get('low'),
                           lastPrice=json_data.get('close'),
                           volume=json_data.get('amount'),
                           quoteVolume=json_data.get('vol'),
                           closeTime=full_json_data.get('ts'),
                           )]
        else:
            raise Exception(json_data)

        return Response(data=data, response_object=response)

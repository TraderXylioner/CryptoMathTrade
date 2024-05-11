from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
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
        if 'limit' in params:
            params['depth'] = params['limit']
            params.pop('limit')
        if 'type' not in params:
            params['type'] = 'step0'
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List

        GET /market/history/trade

        https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 1; max 2000.
        """
        if 'limit' in params:
            params['size'] = params['limit']
            params.pop('limit')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /market/detail/merged or /market/tickers

        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
        or
        https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in params else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: market.{symbol}.depth.{type}

        https://www.htx.com/en-us/opend/newApiPages/?id=7ec5342e-7773-11ed-9966-0242ac110003

        param:
            symbol (str): the trading pair

            type (str, optional): Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5. Default step0.

        when type is set to "step0", the default value of "depth" is 150 instead of 20.

        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000

        """
        return self.return_args(method='sub',
                                url=URLS.WS_BASE_URL,
                                params=f'market.{params["symbol"].lower()}.depth.{params["type"]}',
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: market.{symbol}.trade.detail

         https://www.htx.com/en-us/opend/newApiPages/?id=7ec53b69-7773-11ed-9966-0242ac110003

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='sub',
                                url=URLS.WS_BASE_URL,
                                params=f'market.{params["symbol"].lower()}.trade.detail',
                                )

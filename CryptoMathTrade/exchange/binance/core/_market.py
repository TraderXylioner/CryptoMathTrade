from .._urls import URLS
from ..._core import Core
from ...errors import ParameterRequiredError
from ...utils import check_require_params, convert_list_to_json_array


class MarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    def get_trades_args(self, **kwargs) -> dict:
        """Recent Trades List

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker_args(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair

            or / and

            symbols (list, optional): list of trading pairs
        """
        if not kwargs.get('symbol') and not kwargs.get('symbols'):
            raise ParameterRequiredError(['symbol', 'symbols'])

        if kwargs.get('symbol') and kwargs.get('symbols'):
            kwargs['symbols'].append(kwargs['symbol'])
            kwargs.pop('symbol')

        if kwargs.get('symbols'):
            kwargs['symbols'] = convert_list_to_json_array(kwargs.get('symbols'))
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=kwargs)


class WSMarketCore(Core):
    def get_depth_args(self, **kwargs) -> dict:
        """Partial Book Depth Streams

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        https://binance-docs.github.io/apidocs/spot/en/#partial-book-depth-streams

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

            interval (int, optional): 1000ms or 100ms.
        """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='SUBSCRIBE',
                                url=URLS.WS_BASE_URL,
                                params=[f'{kwargs["symbol"].lower()}@depth{kwargs["limit"]}@{kwargs["interval"]}ms'],
                                )

    def get_trades_args(self, **kwargs) -> dict:
        """Trade Streams

         Update Speed: Real-time

         Stream Name: <symbol>@trade

         https://binance-docs.github.io/apidocs/spot/en/#trade-streams

         params:
            symbol (str): the trading pair
         """
        check_require_params(kwargs, ('symbol',))
        return self.return_args(method='SUBSCRIBE', url=URLS.WS_BASE_URL, params=[f'{kwargs["symbol"].lower()}@trade'])

from .._api import API
from .._urls import URLS
from ...utils import get_timestamp, check_require_params


class MarketCore(API):
    def get_depth(self, **kwargs) -> dict:
        """Get orderbook.

        GET /openApi/spot/v1/market/depth

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information

        param:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 1000.
        """
        check_require_params(kwargs, ('symbol',))
        kwargs['limit'] = min(int(kwargs.get('limit', 100)), 1000)  # Default value and limit
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=kwargs)

    def get_trades(self, **kwargs) -> dict:
        """Recent Trades List

        GET /openApi/spot/v1/market/trades

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 100.
        """
        check_require_params(kwargs, ('symbol',))
        kwargs['limit'] = min(int(kwargs.get('limit', 100)), 100)  # Default value and limit
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=kwargs)

    def get_ticker(self, **kwargs) -> dict:
        """24hr Ticker Price Change Statistics

        GET /openApi/spot/v1/ticker/24hr

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes

        params:
            symbol (str, optional): the trading pair.
        """
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=kwargs)

    def get_symbols(self, **kwargs) -> dict:
        """Query Symbols

        GET /openApi/spot/v1/common/symbols

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols

        params:
            symbol (str, optional): the trading pair.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=kwargs)

    def get_kline(self, **kwargs) -> dict:
        """Historical K-line data

        GET /openApi/market/his/v1/kline

        https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            limit (int, optional): Default 500; max 1000.
        """
        kwargs['limit'] = min(int(kwargs.get('limit', 500)), 1000)  # Default value and limit
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.KLINE_URL, params=kwargs)


class WSMarketCore(API):
    def get_depth(self, **kwargs) -> dict:
        """Partial Book Depth Streams

        Stream Names: {symbol}@depth{limit}

        https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscribe%20Market%20Depth%20Data

        param:
            symbol (str): the trading pair.

            limit (int, optional): Valid are 10, 20 or 50.
        """

        return self.return_args(method='sub',
                                url=URLS.WS_BASE_URL,
                                params=f'{kwargs["symbol"].upper()}@depth{kwargs["limit"]}',
                                )

    def get_trades(self, **kwargs) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: {symbol}@trade

         https://bingx-api.github.io/docs/#/en-us/spot/socket/market.html#Subscription%20transaction%20by%20transaction

         param:
            symbol (str): the trading pair.
         """
        return self.return_args(method='sub', url=URLS.WS_BASE_URL, params=f'{kwargs["symbol"].upper()}@trade')

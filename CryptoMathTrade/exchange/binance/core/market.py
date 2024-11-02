from ..api.api import API
from ..urls import URLS
from ...utils import check_require_params, convert_list_to_json_array


class MarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://binance-docs.github.io/apidocs/spot/en/#order-book

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 100; max 5000.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.DEPTH_URL, params=params
        )

    @check_require_params(("symbol",))
    def get_trades(self, **params) -> dict:
        """Recent Trades List

        GET /api/v3/trades

        https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

        params:
            symbol (str): the trading pair.

            limit (int, optional): Default 500; max 1000.
        """
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.TRADES_URL, params=params
        )

    def get_ticker(self, **params) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair.

            or / and

            symbols (list, optional): list of trading pairs.
        """
        if params.get("symbol") and params.get("symbols"):
            params["symbols"].append(params["symbol"])
            params.pop("symbol")

        if params.get("symbols"):
            params["symbols"] = convert_list_to_json_array(params.get("symbols"))
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.TICKER_URL, params=params
        )

    def get_symbols(self, **params) -> dict:
        """Query Symbols

        GET /api/v3/exchangeInfo

        https://binance-docs.github.io/apidocs/spot/en/#exchange-information

        params:
            symbol (str, optional): the trading pair.

            or / and

            symbols (list, optional): list of trading pairs.
        """
        if params.get("symbol") and params.get("symbols"):
            params["symbols"].append(params["symbol"])
            params.pop("symbol")

        if params.get("symbols"):
            params["symbols"] = convert_list_to_json_array(params.get("symbols"))
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.SYMBOLS_URL, params=params
        )

    @check_require_params(("symbol", "interval"))
    def get_kline(self, **params) -> dict:
        """Historical K-line data

        GET /api/v3/klines

        https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

        params:
            symbol (str): the trading pair.

            interval (str): Time interval (1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M).

            limit (int, optional): Default 500; max 1000.

            startTime (int, optional): Unit: ms.

            endTime (int, optional): Unit: ms.

            timeZone (str, optional): Default: 0 (UTC).
        """
        params["limit"] = min(
            int(params.get("limit", 500)), 1000
        )  # Default value and limit
        return self.return_args(
            method="GET", url=URLS.BASE_URL + URLS.KLINE_URL, params=params
        )


class WebSocketMarketCore(API):
    @check_require_params(("symbol",))
    def get_depth(self, **params) -> dict:
        """Partial Book Depth Streams

        Stream Names: <symbol>@depth<levels> OR <symbol>@depth<levels>@100ms.

        https://binance-docs.github.io/apidocs/spot/en/#partial-book-depth-streams

        params:
            symbol (str): the trading pair.

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

            interval (int, optional): 1000ms or 100ms.
        """
        return self.return_args(
            method="SUBSCRIBE",
            url=URLS.WS_BASE_URL,
            params=[
                f'{params["symbol"].lower()}@depth{params["limit"]}@{params["interval"]}ms'
            ],
        )

    @check_require_params(("symbol",))
    def get_trades(self, **params) -> dict:
        """Trade Streams

        Update Speed: Real-time

        Stream Name: <symbol>@trade

        https://binance-docs.github.io/apidocs/spot/en/#trade-streams

        params:
           symbol (str): the trading pair.
        """
        return self.return_args(
            method="SUBSCRIBE",
            url=URLS.WS_BASE_URL,
            params=[f'{params["symbol"].lower()}@trade'],
        )

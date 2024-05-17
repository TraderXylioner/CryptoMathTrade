from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 100; max 5000. If limit > 5000, then the response will truncate to 5000.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 500).

        GET /api/v3/trades

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 500; max 1000.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TICKER_URL, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: spot@public.limit.depth.v3.api@<symbol>@<level>.

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#partial-book-depth-streams

        param:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 10, or 20.

        """

        return self.return_args(method='SUBSCRIPTION',
                                url=URLS.WS_BASE_URL,
                                params=f'spot@public.limit.depth.v3.api@{params["symbol"].upper()}@{params["limit"]}',
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot@public.deals.v3.api@<symbol>

         https://mexcdevelop.github.io/apidocs/spot_v3_en/#trade-streams

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='SUBSCRIPTION',
                                url=URLS.WS_BASE_URL,
                                params=f'spot@public.deals.v3.api@{params["symbol"].upper()}',
                                )


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params):
        """Query Assets

        GET /api/v3/account

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#account-information
        """
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(params),
                                )

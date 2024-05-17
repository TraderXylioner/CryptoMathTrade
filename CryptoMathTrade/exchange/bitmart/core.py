from ._urls import URLS
from .._core import Core
from ..utils import _convert_kwargs_to_dict


class MarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Get orderbook.

        GET /spot/quotation/v3/books

        https://developer-pro.bitmart.com/en/spot/#get-depth-v3

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 35; max 50.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.DEPTH_URL, params=params)

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Recent Trades List
        Get recent trades (up to last 50).

        GET /spot/quotation/v3/trades

        https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3

        params:
            symbol (str): the trading pair

            limit (int, optional): limit the results. Default 50; max 50.
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.TRADES_URL, params=params)

    @_convert_kwargs_to_dict
    def get_ticker_args(self, params: dict) -> dict:
        """24hr Ticker Price Change Statistics

        GET /spot/quotation/v3/ticker or /spot/quotation/v3/tickers

        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
        or
        https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3

        params:
            symbol (str, optional): the trading pair, if the symbol is not sent, tickers for all symbols will be returned in an array.
        """
        _url = URLS.TICKER_URL if 'symbol' in params else URLS.TICKERS_URL
        return self.return_args(method='GET', url=URLS.BASE_URL + _url, params=params)


class WSMarketCore(Core):
    @_convert_kwargs_to_dict
    def get_depth_args(self, params: dict) -> dict:
        """Partial Book Depth Streams

        Stream Names: spot/depth{limit}:{symbol}

        https://developer-pro.bitmart.com/en/spot/#public-depth-all-channel

        param:

            symbol (str): the trading pair

            limit (int, optional): limit the results. Valid are 5, 20 or 50.

        """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=f'spot/depth{params["limit"]}:{params["symbol"]}',
                                )

    @_convert_kwargs_to_dict
    def get_trades_args(self, params: dict) -> dict:
        """Trade Streams

         The Trade Streams push raw trade information; each trade has a unique buyer and seller.
         Update Speed: Real-time

         Stream Name: spot/trade:{symbol}

        https://developer-pro.bitmart.com/en/spot/#public-trade-channel-2

         param:
            symbol (str): the trading pair
         """
        return self.return_args(method='subscribe',
                                url=URLS.WS_BASE_URL,
                                params=f'spot/trade:{params["symbol"]}',
                                )


class AccountCore(Core):
    @_convert_kwargs_to_dict
    def get_balance_args(self, AccountObj, params):
        """Query Assets

        GET /account/v1/wallet

        https://developer-pro.bitmart.com/en/spot/#get-account-balance-keyed

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        if 'asset' in params:
            params['currency'] = params['asset']
            params.pop('asset')
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_BALANCE,
                                params=AccountObj.get_payload(params),
                                )

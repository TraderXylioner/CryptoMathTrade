from .api import API
from .setting import DEPTH_URL, TRADES_URL, PRICE_URL, TICKER_URL
from ..utils import convert_list_to_json_array


class Market(API):
    def get_depth(self, symbol: str, limit: int | None = None):
        params = {'symbol': symbol, 'limit': limit}
        return self._query(DEPTH_URL, params)

    def get_trades(self, symbol: str, limit: int | None = None):
        params = {'symbol': symbol, 'limit': limit}
        return self._query(TRADES_URL, params)

    def get_price(self,
                  symbol: str | None = None,
                  symbols: list | None = None):
        params = {'symbol': symbol, 'symbols': convert_list_to_json_array(symbols)}
        return self._query(PRICE_URL, params)

    def get_ticker(self,
                   symbol: str | None = None,
                   symbols: list | None = None):
        if symbol and symbols:
            raise ValueError('symbol and symbols cannot be sent together.')
        params = {'symbol': symbol, 'symbols': convert_list_to_json_array(symbols)}
        return self._query(TICKER_URL, params)


class AsyncMarket:
    ...

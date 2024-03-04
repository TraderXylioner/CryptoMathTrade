from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /api/v5/market/books

        https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default ; max 400.
        """
        if 'symbol' in params:
            params['instId'] = params.pop('symbol')
        if 'limit' in params:
            params['sz'] = params.pop('limit')

        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

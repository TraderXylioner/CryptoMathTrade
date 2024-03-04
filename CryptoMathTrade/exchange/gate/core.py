from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /api/v4/spot/order_book

        https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results.
            interval (int, optional): Order depth. 0 means no aggregation is applied. default to 0.
        """

        if 'symbol' in params:
            params['currency_pair'] = params.pop('symbol')

        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

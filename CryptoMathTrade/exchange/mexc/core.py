from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /api/v3/depth

        https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 100; max 5000.
        """
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

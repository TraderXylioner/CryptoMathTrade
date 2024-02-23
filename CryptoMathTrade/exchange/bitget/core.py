from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /api/v2/spot/market/orderbook

        https://www.bitget.com/api-doc/spot/market/Get-Orderbook

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default 150; max 150.
            type (str, optional) The value enums：step0，step1，step2，step3，step4，step5. Default: step0.
        """
        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

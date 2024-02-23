from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET /spot/v1/symbols/book

        https://developer-pro.bitmart.com/en/spot/#get-depth-v1

        param:
            symbol (str): the trading pair
            limit (int, optional): limit the results. Default ; max 400.
            precision (int, optional): 	Price precision, the range is defined in trading pair detail.

        Instruction
        precision is optional. If not passed, the default is to use price_max_precision returned by symbols details.
        If the size is left blank, default 50 of data will be returned. If size is larger than '50', error code will be returned.
        """

        if 'limit' in params:
            params['size'] = params.pop('limit')

        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

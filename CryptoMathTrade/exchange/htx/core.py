from ._urls import URLS
from ..utils import _convert_kwargs_to_dict


class Core:
    # Market
    @classmethod
    @_convert_kwargs_to_dict
    def get_depth_args(cls, params: dict) -> dict:
        """Get orderbook.

        GET market/depth

        https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth

        param:
            symbol (str): the trading pair
            type (str, optional) Market depth aggregation level. Value Range: step0, step1, step2, step3, step4, step5. default: step0
            limit (int, optional) The number of market depth to return on each side	5, 10, 20 default: 	20

        when type is set to "step0", the default value of "depth" is 150 instead of 20.
        "type" Details

        Value	Description
        step0	No market depth aggregation
        step1	Aggregation level = precision*10
        step2	Aggregation level = precision*100
        step3	Aggregation level = precision*1000
        step4	Aggregation level = precision*10000
        step5	Aggregation level = precision*100000
        """
        if 'limit' in params:
            params['depth'] = params.pop('limit')
        if 'type' not in params:
            params['type'] = 'step0'

        return {'method': 'GET', 'url': URLS.BASE_URL + URLS.DEPTH_URL, 'params': params}

from .._urls import URLS
from ..._core import Core
from ...utils import _convert_kwargs_to_dict


class SpotCore(Core):
    @_convert_kwargs_to_dict
    def get_orders_args(self, SpotObj, params):
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def get_open_order_args(self, SpotObj, params):
        if not params.get('orderId') and not params.get('origClientOrderId'):
            raise ValueError('Param "origClientOrderId" or "orderId" must be sent, but both were empty/null!')
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.ORDER_URL, params=SpotObj.get_payload(params))

    @_convert_kwargs_to_dict
    def get_open_orders_args(self, SpotObj, params):
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.OPEN_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def cancel_open_order_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDER_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def cancel_open_orders_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST',
                                url=URLS.BASE_URL + URLS.CANCEL_ORDERS_URL,
                                params=SpotObj.get_payload(params),
                                )

    @_convert_kwargs_to_dict
    def new_order_args(self, SpotObj, params: dict) -> dict:
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.CREATE_ORDER_URL,
                                params=SpotObj.get_payload(params))

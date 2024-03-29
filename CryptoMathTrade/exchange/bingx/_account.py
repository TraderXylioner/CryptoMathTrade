from ._api import API
from .core import AccountCore
from .._response import Response
from ..utils import validate_response


class Account(API):
    def get_balance(self, recvWindow: int | None = None):
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets

        params:
            recvWindow (int, optional): The value cannot be greater than 60000
        """
        response = validate_response(self._query(**AccountCore(headers=self.headers).get_balance_args(self,
                                                                                                      recvWindow=recvWindow,
                                                                                                      )))
        json_data = response.json()['data']
        return Response(data=json_data,
                        response_object=response,
                        )

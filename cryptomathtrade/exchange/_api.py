import asyncio

from ._request import Request, AsyncRequest, WebSocketRequest
from .utils import check_api_keys, hmac_hashing, _prepare_params, get_timestamp


class BaseAPI:
    def __init__(self,
                 api_key=None,
                 api_secret=None,
                 headers=None,
                 ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {}
        if headers:
            self.headers.update(headers)

    def _query(self,
               url: str,
               params: dict = None,
               method: str = 'GET',
               ):
        """
        params:
            url (str): URL for the API endpoint.

            params (dict): Query parameters for the API request.

            method (str): HTTP method for the request (default is 'GET').
        """
        return Request(headers=self.headers).send_request(method, url, params)

    async def _async_query(self,
                           url: str,
                           params: dict = None,
                           method: str = 'GET',
                           ):
        """
        params:
            url (str): URL for the API endpoint.

            params (dict): Query parameters for the API request.

            method (str): HTTP method for the request (default is 'GET').
        """
        return await AsyncRequest(headers=self.headers).send_request(method, url, params)

    async def _ws_query(self,
                        url: str,
                        params: str,
                        method: str = 'SUBSCRIBE',
                        timeout_seconds=60,
                        ):
        """
        params:
            url (str): WebSocket URL for the API.

            params (str): Parameters for the WebSocket request.

            method (str): Method for the WebSocket request (default is 'SUBSCRIBE').

            timeout_seconds (int): Timeout duration for the WebSocket connection.
        """
        payload = {
            "method": method,
            "params": params,
        }
        connect = WebSocketRequest(headers=self.headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                yield data

    @check_api_keys
    def get_payload(self, payload=None):
        """
          params:
              payload (dict): Additional payload parameters.

          Returns:
              dict: Payload with timestamp and signature.
          """
        if payload is None:
            payload = {}
        payload['timestamp'] = get_timestamp()
        query_string = _prepare_params(payload)
        payload['signature'] = self._get_sign(query_string)
        return payload

    def _get_sign(self, payload: dict):
        """
        params:
            payload (dict): Payload data for generating signature.

        Returns:
            str: HMAC signature.
        """
        return hmac_hashing(self.api_secret, payload)

    def return_args(self, **kwargs):
        # if self.headers:
        #     kwargs['headers'] = self.headers
        return kwargs

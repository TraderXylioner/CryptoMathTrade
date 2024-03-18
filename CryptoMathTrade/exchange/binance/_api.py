import asyncio
import json

from .._request import Request, AsyncRequest, WebSocketRequest
from ..utils import get_timestamp, hmac_hashing, _prepare_params, check_api_keys


class API:
    def __init__(self, api_key=None, api_secret=None, headers=None):
        """
        params:
            api_key (str): API key for authentication.
            api_secret (str): API secret for authentication.
            headers (dict): Additional headers for API requests.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'X-MBX-APIKEY': self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @classmethod
    def _query(cls,
               url: str,
               params: dict,
               method: str = 'GET',
               headers=None,
               ):
        """
        params:
            url (str): URL for the API endpoint.

            params (dict): Query parameters for the API request.

            method (str): HTTP method for the request (default is 'GET').

            headers (dict): Additional headers for the request.
        """
        return Request(headers=headers).send_request(method, url, params)

    @classmethod
    async def _async_query(cls,
                           url: str,
                           params: dict,
                           method: str = 'GET',
                           headers=None,
                           ):
        """
        params:
            url (str): URL for the API endpoint.

            params (dict): Query parameters for the API request.

            method (str): HTTP method for the request (default is 'GET').

            headers (dict): Additional headers for the request.
        """
        return await AsyncRequest(headers=headers).send_request(method, url, params)

    @classmethod
    async def _ws_query(cls,
                        url: str,
                        params: str,
                        method: str = 'SUBSCRIBE',
                        timeout_seconds=10,
                        headers=None,
                        ):
        """
        params:
            url (str): WebSocket URL for the API.

            params (str): Parameters for the WebSocket request.

            method (str): Method for the WebSocket request (default is 'SUBSCRIBE').

            timeout_seconds (int): Timeout duration for the WebSocket connection.

            headers (dict): Additional headers for the request.
        """
        payload = {
            "method": method,
            "params": [params],
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                json_data = json.loads(data)
                yield json_data

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

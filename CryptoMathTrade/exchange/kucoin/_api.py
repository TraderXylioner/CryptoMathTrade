import asyncio
import base64
import hashlib
import hmac
import json

from .._api import BaseAPI
from .._request import WebSocketRequest
from ..utils import check_api_keys, get_timestamp


class API(BaseAPI):
    def __init__(self, api_key=None, api_secret=None, passphrase=None, headers=None):
        """
        params:
            api_key (str): API key for authentication.

            api_secret (str): API secret for authentication.

            headers (dict): Additional headers for API requests.
        """
        super().__init__()
        self.api_key = api_key
        self.api_secret = api_secret
        self.passphrase = passphrase
        self.headers = {'KC-API-KEY': self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @classmethod
    async def _ws_query(cls,
                        url: str,
                        params: str,
                        method: str = 'subscribe',
                        timeout_seconds=60,
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
            "type": method,
            "topic": params,
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                yield data

    @classmethod
    def toQueryWithNoEncode(cls, params):
        url = ''
        for key, value in params:
            url = url + str(key) + '=' + str(value) + '&'
        return url[0:-1]

    @classmethod
    def parse_params_to_str(cls, params):
        params = [(key, val) for key, val in params.items()]
        params.sort(key=lambda x: x[0])
        url = '?' + cls.toQueryWithNoEncode(params)
        if url == '?':
            return ''
        return url

    @check_api_keys
    def get_payload(self, path: str, method: str, payload: dict = None):
        """
          params:
              payload (dict): Additional payload parameters.

          Returns:
              dict: Payload with timestamp and signature.
          """
        t = str(get_timestamp())
        str_to_sign = t + method.upper() + path
        if payload:
            str_to_sign += self.parse_params_to_str(payload)
        signature = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())

        passphrase = base64.b64encode(
            hmac.new(self.api_secret.encode('utf-8'), self.passphrase.encode('utf-8'), hashlib.sha256).digest())
        return {"KC-API-SIGN": signature,
                "KC-API-TIMESTAMP": t,
                "KC-API-KEY": self.api_key,
                "KC-API-PASSPHRASE": passphrase,
                "KC-API-KEY-VERSION": "2",
                "Content-Type": "application/json",
                }

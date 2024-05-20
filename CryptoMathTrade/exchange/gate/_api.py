import asyncio
import hashlib
import hmac
import json
import time

from .._api import BaseAPI
from .._request import WebSocketRequest
from ..utils import check_api_keys, get_timestamp, _prepare_params


class API(BaseAPI):
    def __init__(self, api_key=None, api_secret=None, headers=None):
        """
        params:
            api_key (str): API key for authentication.

            api_secret (str): API secret for authentication.

            headers (dict): Additional headers for API requests.
        """
        super().__init__()
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'KEY': self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @classmethod
    async def _ws_query(cls,
                        url: str,
                        params: dict,
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
            "event": method,
            "payload": params.get('payload'),
            "channel": params.get('channel'),
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                yield data

    def _get_sign(self, message: str):
        sign = hmac.new(self.api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha512).hexdigest()
        return sign

    @check_api_keys
    def get_payload(self, path: str, method: str, payload: dict = None):
        """
          params:
              payload (dict): Additional payload parameters.

          Returns:
              dict: Payload with timestamp and signature.
          """
        if payload:
            payload = _prepare_params(payload)
        else:
            payload = ""
        t = time.time()
        m = hashlib.sha512()
        hashed_payload = m.hexdigest()
        message = '%s\n%s\n%s\n%s\n%s' % (method, path, payload, hashed_payload, t)
        return {'KEY': self.api_key,
                'Timestamp': str(t),
                'SIGN': self._get_sign(message),
                }

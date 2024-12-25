import asyncio
import base64
import datetime
import hmac

from ..._api import BaseAPI
from ..._request import WebSocketRequest
from ...utils import check_api_keys


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
        self.headers = {"OK-ACCESS-KEY": self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @classmethod
    async def _ws_query(
        cls,
        url: str,
        params: dict,
        method: str = "subscribe",
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
            "op": method,
            "args": params,
        }
        connect = WebSocketRequest(headers=headers).open_connect(
            url=url, payload=payload
        )
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                yield data

    @classmethod
    def pre_hash(cls, timestamp, method, request_path, body):
        return str(timestamp) + str.upper(method) + request_path + body

    def _get_sign(self, message: str):
        mac = hmac.new(
            bytes(self.api_secret, encoding="utf8"),
            bytes(message, encoding="utf-8"),
            digestmod="sha256",
        )
        d = mac.digest()
        return base64.b64encode(d)

    @check_api_keys
    def get_payload(self, path: str, method: str, payload: dict = None):
        """
        params:
            payload (dict): Additional payload parameters.

        Returns:
            dict: Payload with timestamp and signature.
        """
        if payload is None:
            payload = {}
        now = datetime.datetime.utcnow()
        t = now.isoformat("T", "milliseconds")
        timestamp = t + "Z"
        sign = self._get_sign(self.pre_hash(timestamp, method, path, ""))
        return {
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-SIGN": sign,
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": self.passphrase,
        }

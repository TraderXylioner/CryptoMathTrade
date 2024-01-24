import asyncio
import json

from CryptoMathTrade.exchange._request import Request, AsyncRequest, WebSocketRequest
from ..utils import get_timestamp, rsa_signature, hmac_hashing, _prepare_params, ed25519_signature, check_api_keys


class API:
    def __init__(self, api_key=None, api_secret=None, private_key=None, private_key_pass=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.private_key = private_key
        self.private_key_pass = private_key_pass
        self.headers = {'X-MBX-APIKEY': self.api_key} if self.api_key else {}

    def _query(self, url, params, method: str = 'GET', headers=None):
        if headers:
            self.headers.update(headers)
        return Request(headers=self.headers).send_request(method, url, params)

    async def _async_query(self, url, params, method: str = 'GET', headers=None):
        if headers:
            self.headers.update(headers)
        return await AsyncRequest(headers=self.headers).send_request(method, url, params)

    @classmethod
    async def _ws_query(cls, url: str, params: str, method: str = 'SUBSCRIBE', timeout_seconds=10):
        payload = {
            "method": method,
            "params": [params],
        }
        connect = WebSocketRequest().open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError
                json_data = json.loads(data)
                yield json_data

    @check_api_keys
    def get_payload(self, payload=None):
        if payload is None:
            payload = {}
        payload['timestamp'] = get_timestamp()
        query_string = _prepare_params(payload)
        payload['signature'] = self._get_sign(query_string)
        return payload

    def _get_sign(self, payload):
        if self.private_key is not None:
            try:
                return ed25519_signature(
                    self.private_key, payload, self.private_key_pass
                )
            except ValueError:
                return rsa_signature(self.private_key, payload, self.private_key_pass)
        else:
            return hmac_hashing(self.api_secret, payload)

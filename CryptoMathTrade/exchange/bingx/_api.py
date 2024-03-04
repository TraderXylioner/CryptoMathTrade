import asyncio
import gzip
import io
import json
import uuid

from .._request import Request, AsyncRequest, WebSocketRequest
from ..utils import get_timestamp, hmac_hashing, _prepare_params, check_api_keys


class API:
    def __init__(self, api_key=None, api_secret=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'X-BX-APIKEY': self.api_key} if self.api_key else {}

    def _query(self, url: str, params: dict, method: str = 'GET', headers=None):
        if headers:
            self.headers.update(headers)
        return Request(headers=self.headers).send_request(method, url, params)

    async def _async_query(self, url: str, params: dict, method: str = 'GET', headers=None):
        if headers:
            self.headers.update(headers)
        return await AsyncRequest(headers=self.headers).send_request(method, url, params)

    @classmethod
    async def _ws_query(cls, url: str, params: str, method: str = 'sub', timeout_seconds=10):
        payload = {
            "method": method,
            "dataType": params,
            'id': str(uuid.uuid4())
        }
        connect = WebSocketRequest().open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                await client.send('Pong')
                decompressed_data = gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb').read().decode('utf-8')
                json_data = json.loads(decompressed_data)
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
        return hmac_hashing(self.api_secret, payload)

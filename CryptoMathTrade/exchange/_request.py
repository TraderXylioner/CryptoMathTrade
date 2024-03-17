import json
import websockets
import aiohttp
import requests

from .utils import clean_none_value, _prepare_params, _dispatch_request


class Request:
    def __init__(self, timeout=None, proxies=None, headers=None):
        self.session = requests.Session()
        self.timeout = timeout
        self.proxies = proxies
        if headers:
            self.session.headers.update(headers)

    def send_request(self, method: str, url: str, payload=None):
        if payload is None:
            payload = {}
        params = clean_none_value({'url': url,
                                   'params': _prepare_params(payload),
                                   'timeout': self.timeout,
                                   'proxies': self.proxies,
                                   })
        response = _dispatch_request(self.session, method)(**params)
        return response


class AsyncRequest:
    def __init__(self, timeout=None, proxies=None, headers=None):
        self.timeout = timeout
        self.proxies = proxies
        self.headers = headers

    async def send_request(self, method: str, url: str, payload: dict | None = None):
        if payload is None:
            payload = {}
        params = clean_none_value({'url': url,
                                   'params': clean_none_value(payload),
                                   'timeout': self.timeout,
                                   'proxies': self.proxies,
                                   })
        async with aiohttp.ClientSession() as session:
            async with _dispatch_request(session, method)(**params) as response:
                response.json = await response.json()
                return response


class WebSocketRequest:
    @classmethod
    async def open_connect(cls, url: str, payload: dict):
        async with websockets.connect(url) as client:
            await client.send(json.dumps(payload))
            yield client

import aiohttp
import requests

from CryptoMathTrade.exchange.utils import clean_none_value, _prepare_params


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
        response = self._dispatch_request(method)(**params)
        return response

    def _dispatch_request(self, http_method):
        return {
            'GET': self.session.get,
            'DELETE': self.session.delete,
            'PUT': self.session.put,
            'POST': self.session.post,
        }.get(http_method, 'GET')


# class AsyncRequest:
#     @classmethod
#     async def send_async_request(cls,
#                                  url: str,
#                                  headers: dict | None = None,
#                                  proxy: str | None = None
#                                  ):
#         async with aiohttp.ClientSession(headers=headers) as session:
#             async with session.get(url=url, proxy=proxy, ssl=True) as response:
#                 print(response)
#                 response = await response.json()
#                 print(response)

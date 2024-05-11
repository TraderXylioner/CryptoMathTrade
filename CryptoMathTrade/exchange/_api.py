import asyncio

from ._request import Request, AsyncRequest, WebSocketRequest


class BaseAPI:
    def __init__(self, headers=None):
        self.headers = {}
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
            "method": method,
            "params": [params],
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                yield data

import asyncio
import uuid

from .._request import WebSocketRequest
from .._api import BaseAPI


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
        self.headers = {'X-BX-APIKEY': self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @classmethod
    async def _ws_query(cls,
                        url: str,
                        params: str,
                        method: str = 'sub',
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
            "reqType": method,
            "dataType": params,
            'id': str(uuid.uuid4())
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                await client.send('Pong')
                yield data

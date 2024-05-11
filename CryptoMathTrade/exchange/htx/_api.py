import asyncio
import gzip
import json

from .._api import BaseAPI
from .._request import WebSocketRequest


class API(BaseAPI):
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
            "method": method,
            "sub": params,
        }
        connect = WebSocketRequest(headers=headers).open_connect(url=url, payload=payload)
        async for client in connect:
            while True:
                data = await asyncio.wait_for(client.recv(), timeout=timeout_seconds)
                if not data:
                    raise ConnectionError  # custom error
                json_data = json.loads(gzip.decompress(data))
                if 'ping' in json_data:
                    await client.send('pong')
                yield data

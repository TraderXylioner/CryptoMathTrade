from .._request import Request, AsyncRequest


class API:
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

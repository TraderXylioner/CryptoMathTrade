from CryptoMathTrade.exchange._api import BaseAPI


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
        self.headers = {"X-MEXC-APIKEY": self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

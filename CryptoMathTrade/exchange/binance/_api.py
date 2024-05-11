from ..utils import get_timestamp, hmac_hashing, _prepare_params, check_api_keys
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
        self.headers = {'X-MBX-APIKEY': self.api_key} if self.api_key else {}
        if headers:
            self.headers.update(headers)

    @check_api_keys
    def get_payload(self, payload=None):
        """
          params:
              payload (dict): Additional payload parameters.

          Returns:
              dict: Payload with timestamp and signature.
          """
        if payload is None:
            payload = {}
        payload['timestamp'] = get_timestamp()
        query_string = _prepare_params(payload)
        payload['signature'] = self._get_sign(query_string)
        return payload

    def _get_sign(self, payload: dict):
        """
        params:
            payload (dict): Payload data for generating signature.

        Returns:
            str: HMAC signature.
        """
        return hmac_hashing(self.api_secret, payload)

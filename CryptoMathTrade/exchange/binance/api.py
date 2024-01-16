from CryptoMathTrade.exchange._request import Request
from .setting import BASE_URL
from ..utils import get_timestamp, rsa_signature, hmac_hashing, _prepare_params, ed25519_signature, check_api_keys


class API:
    def __init__(self, api_key=None, api_secret=None, private_key=None, private_key_pass=None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.private_key = private_key
        self.private_key_pass = private_key_pass

    @classmethod
    def _query(cls, url, params):
        return Request().send_request('GET', BASE_URL + url, params)

    @check_api_keys
    def sign_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        payload["timestamp"] = get_timestamp()
        query_string = _prepare_params(payload)
        payload["signature"] = self._get_sign(query_string)
        return Request(headers={"X-MBX-APIKEY": self.api_key}).send_request(http_method, BASE_URL + url_path, payload)

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

import json
import time
from urllib.parse import urlencode

import hmac
import hashlib

from .errors import ParameterRequiredError


def clean_none_value(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def convert_list_to_json_array(symbols):
    if symbols is None:
        return symbols
    res = json.dumps(symbols)
    return res.replace(' ', '')


def get_timestamp():
    return int(time.time() * 1000)


def hmac_hashing(api_secret, payload):
    return hmac.new(api_secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()


# def rsa_signature(private_key, payload, private_key_pass=None):
#     private_key = RSA.import_key(private_key, passphrase=private_key_pass)
#     h = SHA256.new(payload.encode('utf-8'))
#     signature = pkcs1_15.new(private_key).sign(h)
#     return b64encode(signature)


# def ed25519_signature(private_key, payload, private_key_pass=None):
#     private_key = ECC.import_key(private_key, passphrase=private_key_pass)
#     signer = eddsa.new(private_key, 'rfc8032')
#     signature = signer.sign(payload.encode('utf-8'))
#     return b64encode(signature)


def encoded_string(query):
    return urlencode(query, True).replace('%40', '@')


def _prepare_params(params):
    return encoded_string(clean_none_value(params))


def check_api_keys(func):
    def wrapper(self, *args, **kwargs):
        if not self.api_key or not self.api_secret:
            raise ParameterRequiredError(['API key', 'API secret'])
        return func(self, *args, **kwargs)

    return wrapper


def _dispatch_request(session, http_method):
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')


def _convert_kwargs_to_dict(func):
    def wrapper(*args, **kwargs):
        res = {key: value for key, value in kwargs.items() if value is not None}
        if res.get('symbols'):
            res['symbols'] = convert_list_to_json_array(res.get('symbols'))
        return func(*args, res)

    return wrapper


def validate_response(response):
    if hasattr(response, 'status_code') and response.status_code == 200:
        return response
    elif hasattr(response, 'status') and response.status == 200:
        return response
    else:
        raise Exception(response.__dict__)  # custom exc

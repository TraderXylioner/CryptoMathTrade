from typing import Generic, TypeVar

from pydantic import BaseModel


data = TypeVar('data')
response_object = TypeVar('response_object')


class Response(BaseModel, Generic[data, response_object]):
    """
    Data model for representing an API response.

    params:
        data: The result object of the request.
        response_object: The response object from the server, typically similar
                         to the object obtained from the requests or aiohttp libraries.
    """
    data: data
    response_object: response_object

    def __str__(self):
        return str(self.data)

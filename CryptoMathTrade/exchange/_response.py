from pydantic import BaseModel


class Response(BaseModel):
    """
    Data model for representing an API response.

    params:
        data: The result object of the request.
        response_object: The response object from the server, typically similar
                         to the object obtained from the requests or aiohttp libraries.
    """
    data: object
    response_object: object

from .utils import validate_data
from ..._response import Response
from ....types import Coin, Network


@validate_data
def deserialize_coins(data: dict, response) -> Response[list[Coin], object]:
    data = data["data"]
    return Response(
        data=[
            Coin(
                coin=coin.get("coin"),
                networks=[
                    Network(
                        network=network.get("chain"),
                        name=None,
                        depositEnable=network.get("rechargeable"),
                        withdrawEnable=network.get("withdrawable"),
                        contractAddress=network.get("contractAddress"),
                        browserUrl=network.get("browserUrl"),
                        withdrawFee=network.get("withdrawFee"),
                        extraWithdrawFee=network.get("extraWithdrawFee"),
                        withdrawMin=network.get("minWithdrawAmount"),
                        withdrawMax=None,
                        minConfirm=network.get("withdrawConfirm"),
                        needTagOrMemo=None,
                    )
                    for network in coin.get("chains")
                ],
            )
            for coin in data
        ],
        response_object=response,
    )

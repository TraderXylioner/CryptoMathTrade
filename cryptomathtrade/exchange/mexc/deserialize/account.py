from .utils import validate_data
from ..._response import Response
from ....types import Coin, Network


@validate_data
def deserialize_coins(data, response) -> Response[list[Coin], object]:
    return Response(
        data=[
            Coin(
                coin=coin.get("coin"),
                name=coin.get("name"),
                networks=[
                    Network(
                        network=network.get("netWork"),
                        name=network.get("network"),
                        depositEnable=network.get("depositEnable"),
                        withdrawEnable=network.get("withdrawEnable"),
                        contractAddress=network.get("contract"),
                        browserUrl=None,
                        withdrawFee=network.get("withdrawFee"),
                        extraWithdrawFee=None,
                        withdrawMin=network.get("withdrawMin"),
                        withdrawMax=network.get("withdrawMax"),
                        minConfirm=network.get("minConfirm"),
                        needTagOrMemo=network.get("sameAddress"),
                    )
                    for network in coin.get("networkList")
                ],
            )
            for coin in data
        ],
        response_object=response,
    )

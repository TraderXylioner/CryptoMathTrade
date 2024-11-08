from .utils import validate_data
from ..._response import Response
from ....types import Coin, Network


@validate_data
def deserialize_coins(data, response) -> Response[list[Coin], object]:
    data = data["data"]
    return Response(
        data=[
            Coin(
                coin=coin.get("currency"),
                name=coin.get("fullName"),
                networks=[
                    Network(
                        network=network.get("chainId"),
                        name=network.get("chainName"),
                        depositEnable=network.get("isDepositEnabled"),
                        withdrawEnable=network.get("isWithdrawEnabled"),
                        contractAddress=network.get("contractAddress"),
                        browserUrl=None,
                        withdrawFee=network.get("withdrawalMinFee"),
                        extraWithdrawFee=network.get("withdrawFeeRate"),
                        withdrawMin=network.get("withdrawalMinSize"),
                        withdrawMax=network.get("maxWithdraw"),
                        minConfirm=network.get("confirms"),
                        needTagOrMemo=network.get("needTag"),
                    )
                    for network in coin.get("chains") or []
                ],
            )
            for coin in data
        ],
        response_object=response,
    )

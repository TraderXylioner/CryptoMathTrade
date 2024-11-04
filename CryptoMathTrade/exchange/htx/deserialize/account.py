from .utils import validate_data
from ..._response import Response
from ....types import Coin, Network


@validate_data
def deserialize_coins(data: dict, response) -> Response[list[Coin], object]:
    data = data["data"]
    new_data = {}
    for i in data:
        coin_name = i.get("currency")
        network = Network(
            network=i.get("dn"),
            name=None,
            depositEnable=i.get("de"),
            withdrawEnable=i.get("we"),
            contractAddress=i.get("ca"),
            browserUrl=None,
            withdrawFee=None,
            extraWithdrawFee=None,
            withdrawMin=i.get("wma"),
            withdrawMax=None,
            minConfirm=i.get("sc"),
            needTagOrMemo=i.get("awt"),
        )
        coin = new_data.setdefault(
            coin_name, Coin(coin=coin_name, name=None, networks=[])
        )
        coin.networks.append(network)
    return Response(data=list(new_data.values()), response_object=response)

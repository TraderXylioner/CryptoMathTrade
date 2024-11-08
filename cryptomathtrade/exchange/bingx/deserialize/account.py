from .utils import validate_data
from ..._response import Response
from ...errors import ResponseError
from ....types import (
    Balance,
    Withdraw,
    Coin,
    DepositAddress,
    WithdrawHistory,
    DepositHistory,
    Network,
)


@validate_data
def deserialize_coins(data, response) -> Response[list[Coin], object]:
    data = data["data"]
    return Response(
        data=[
            Coin(
                coin=coin.get("coin"),
                name=coin.get("name"),
                networks=[
                    Network(
                        network=network.get("network"),
                        name=network.get("name"),
                        depositEnable=network.get("depositEnable"),
                        withdrawEnable=network.get("withdrawEnable"),
                        contractAddress=network.get("contractAddress"),
                        browserUrl=None,
                        withdrawFee=network.get("withdrawFee"),
                        extraWithdrawFee=None,
                        withdrawMin=network.get("withdrawMin"),
                        withdrawMax=network.get("withdrawMax"),
                        minConfirm=network.get("minConfirm"),
                        needTagOrMemo=network.get("needTagOrMemo"),
                    )
                    for network in coin.get("networkList")
                ],
            )
            for coin in data
        ],
        response_object=response,
    )


def deserialize_listen_key(data, response) -> Response[str, object]:
    if "listenKey" not in data:
        raise ResponseError(data)
    return Response(data=data["listenKey"], response_object=response)


@validate_data
def deserialize_account_update_for_ws(data, response) -> Response[object, object]:
    return Response(data=data, response_object=response)


@validate_data
def deserialize_deposit_address(
    data, response
) -> Response[list[DepositAddress], object]:
    data = data["data"]
    return Response(
        data=[DepositAddress(**i) for i in data["data"]], response_object=response
    )


@validate_data
def deserialize_withdraw(data, response) -> Response[Withdraw, object]:
    data = data["data"]
    return Response(data=Withdraw(**data), response_object=response)


@validate_data
def deserialize_deposit_history(
    data, response
) -> Response[list[DepositHistory], object]:
    return Response(data=[DepositHistory(**i) for i in data], response_object=response)


@validate_data
def deserialize_withdraw_history(
    data, response
) -> Response[list[WithdrawHistory], object]:
    return Response(data=[WithdrawHistory(**i) for i in data], response_object=response)


@validate_data
def deserialize_balance(data, response) -> Response[list[Balance], object]:
    return Response(
        data=[Balance(**i) for i in data["data"]["balances"]], response_object=response
    )

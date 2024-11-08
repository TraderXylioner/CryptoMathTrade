from ..._response import Response
from ....types import (
    Balance,
    DepositAddress,
    Coin,
    Network,
    DepositHistory,
    WithdrawHistory,
    Withdraw,
)


def deserialize_coins(data, response) -> Response[list[Coin], object]:
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
                        browserUrl=network.get("contractAddressUrl"),
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


def deserialize_balance(data, response) -> Response[list[Balance], object]:
    return Response(data=[Balance(**i) for i in data], response_object=response)


def deserialize_deposit_address(
    data, response
) -> Response[list[DepositAddress], object]:
    return Response(data=[DepositAddress(**data)], response_object=response)


def deserialize_withdraw(data, response) -> Response[Withdraw, object]:
    return Response(data=Withdraw(**data), response_object=response)


def deserialize_deposit_history(
    data, response
) -> Response[list[DepositHistory], object]:
    return Response(data=[DepositHistory(**i) for i in data], response_object=response)


def deserialize_withdraw_history(
    data, response
) -> Response[list[WithdrawHistory], object]:
    return Response(data=[WithdrawHistory(**i) for i in data], response_object=response)

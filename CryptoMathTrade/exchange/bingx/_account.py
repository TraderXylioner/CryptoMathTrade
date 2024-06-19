from ._api import API
from ._serialization import _serialize_balance, _serialize_deposit_address, _serialize_withdraw, _serialize_coins
from .core import AccountCore
from .._response import Response
from ..utils import validate_response


class Account(API):
    def get_balance(self) -> Response:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(self._query(**AccountCore.get_balance(self)))
        json_data = response.json()
        return _serialize_balance(json_data, response)

    def get_deposit_address(self, asset: str, offset: int = None, limit: int = None) -> Response:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            offset (int, optional): Starting record number, default is 0.

            limit (int, optional): Default 100; max 1000.
        """
        response = validate_response(
            self._query(**AccountCore.get_deposit_address(self, asset=asset, offset=offset, limit=limit)))
        json_data = response.json()
        return _serialize_deposit_address(json_data, response)

    def withdraw(self,
                 asset: str,
                 address: str,
                 amount: float,
                 walletType: int,
                 network: str = None,
                 addressTag: str = None,
                 withdrawOrderId: int = None,
                 ):
        """Withdraw

        GET /openApi/wallets/v1/capital/withdraw/apply

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            address (str).

            amount (float).

            walletType (int): Account type: 1 fund account, 2 standard account, 3 perpetual account

            network (str, optional): Use default network if not transmitted.

            addressTag (str, optional): Tag or memo, some currencies support tag or memo.

            withdrawOrderId (str, optional): Customer-defined withdrawal ID, a combination of numbers and letters,
            with a length of less than 100 characters
        """
        response = validate_response(self._query(**AccountCore.withdraw(self,
                                                                        asset=asset,
                                                                        address=address,
                                                                        amount=amount,
                                                                        walletType=walletType,
                                                                        network=network,
                                                                        addressTag=addressTag,
                                                                        withdrawOrderId=withdrawOrderId,
                                                                        )))
        json_data = response.json()
        return _serialize_withdraw(json_data, response)

    def get_coins(self, asset: str = None) -> Response:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        response = validate_response(self._query(**AccountCore.get_coins(self, asset=asset)))
        json_data = response.json()
        return _serialize_coins(json_data, response)


class AsyncAccount(API):
    async def get_balance(self) -> Response:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(await self._async_query(**AccountCore.get_balance(self)))
        json_data = response.json
        return _serialize_balance(json_data, response)

    async def get_deposit_address(self, asset: str, offset: int = None, limit: int = None) -> Response:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            offset (int, optional): Starting record number, default is 0.

            limit (int, optional): Default 100; max 1000.
        """

        response = validate_response(
            await self._async_query(**AccountCore.get_deposit_address(self, asset=asset, offset=offset, limit=limit)))
        json_data = response.json
        return _serialize_deposit_address(json_data, response)

    async def withdraw(self,
                       asset: str,
                       address: str,
                       amount: float,
                       walletType: int,
                       network: str = None,
                       addressTag: str = None,
                       withdrawOrderId: int = None,
                       ):
        """Withdraw

        GET /openApi/wallets/v1/capital/withdraw/apply

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            address (str).

            amount (float).

            walletType (int): Account type: 1 fund account, 2 standard account, 3 perpetual account

            network (str, optional): Use default network if not transmitted.

            addressTag (str, optional): Tag or memo, some currencies support tag or memo.

            withdrawOrderId (str, optional): Customer-defined withdrawal ID, a combination of numbers and letters,
            with a length of less than 100 characters
        """
        response = validate_response(await self._async_query(**AccountCore.withdraw(self,
                                                                                    asset=asset,
                                                                                    address=address,
                                                                                    amount=amount,
                                                                                    walletType=walletType,
                                                                                    network=network,
                                                                                    addressTag=addressTag,
                                                                                    withdrawOrderId=withdrawOrderId,
                                                                                    )))
        json_data = response.json
        return _serialize_withdraw(json_data, response)

    async def get_coins(self, asset: str = None) -> Response:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        response = validate_response(await self._async_query(**AccountCore.get_coins(self, asset=asset)))
        json_data = response.json
        return _serialize_coins(json_data, response)

import gzip
import io
import json
import time

from ._api import API
from ._deserialization import _deserialize_balance, _deserialize_deposit_address, _deserialize_withdraw, \
    _deserialize_coins, \
    _deserialize_deposit_history, _deserialize_account_update_for_ws, _deserialize_listen_key, \
    _deserialize_withdraw_history
from .core import AccountCore, WSAccountCore
from .._response import Response
from ..utils import validate_response
from ...types import Balance, DepositAddress, Withdraw, Coin, DepositHistory, WithdrawHistory


class Account(API):
    def generate_listen_key(self) -> Response[str, object]:
        """Generate Listen Key

        GET openApi/user/auth/userDataStream

        https://bingx-api.github.io/docs/#/en-us/spot/socket/listenKey.html#generate%20Listen%20Key
        """
        response = validate_response(self._query(**AccountCore.generate_listen_key(self)))
        json_data = response.json()
        return _deserialize_listen_key(json_data, response)

    def get_balance(self) -> Response[list[Balance], object]:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(self._query(**AccountCore.get_balance(self)))
        json_data = response.json()
        return _deserialize_balance(json_data, response)

    def get_deposit_address(self,
                            asset: str,
                            limit: int = None,
                            offset: int = None,
                            ) -> Response[list[DepositAddress], object]:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Main%20Account%20Deposit%20Address

        params:
            asset (str).

            limit (int, optional): Default 100; max 1000.

            offset (int, optional): Starting record number, default is 0.
        """
        response = validate_response(
            self._query(**AccountCore.get_deposit_address(self, asset=asset, limit=limit, offset=offset)))
        json_data = response.json()
        return _deserialize_deposit_address(json_data, response)

    def withdraw(self,
                 asset: str,
                 address: str,
                 amount: float,
                 walletType: int,
                 network: str = None,
                 addressTag: str = None,
                 withdrawOrderId: int = None,
                 ) -> Response[Withdraw, object]:
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
        return _deserialize_withdraw(json_data, response)

    def get_coins(self, asset: str = None) -> Response[list[Coin], object]:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        response = validate_response(self._query(**AccountCore.get_coins(self, asset=asset)))
        json_data = response.json()
        return _deserialize_coins(json_data, response)

    def get_deposit_history(self,
                            asset: str = None,
                            limit: int = None,
                            status: int = None,
                            startTime: int = None,
                            endTime: int = None,
                            offset: int = None,
                            ) -> Response[list[DepositHistory], object]:
        """Deposit History

        GET /openApi/api/v3/capital/deposit/hisrec

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Deposit%20History(supporting%20network)

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            status (int, optional): 0-In progress 6-Chain uploaded 1-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.

        """
        response = validate_response(self._query(
            **AccountCore.get_deposit_history(self, asset=asset, limit=limit, status=status, startTime=startTime,
                                              endTime=endTime, offset=offset)))
        json_data = response.json()
        return _deserialize_deposit_history(json_data, response)

    def get_withdraw_history(self,
                             id: str = None,
                             asset: str = None,
                             limit: int = None,
                             withdrawOrderId: str = None,
                             status: int = None,
                             startTime: int = None,
                             endTime: int = None,
                             offset: int = None,
                             ) -> Response[list[WithdrawHistory], object]:
        """Withdraw History

        GET /openApi/api/v3/capital/withdraw/history

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw%20History%20(supporting%20network)

        params:
            id (str, optional): Unique id of the withdrawal record returned by the platform.

            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            withdrawOrderId (str, optional): Custom ID, if there is none, this field will not be returned,When both the platform ID and withdraw order ID are passed as parameters, the query will be based on the platform ID

            status (int, optional):	4-Under Review 5-Failed 6-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.

        """
        response = validate_response(self._query(
            **AccountCore.get_withdraw_history(self, id=id, asset=asset, limit=limit, withdrawOrderId=withdrawOrderId,
                                               status=status, startTime=startTime, endTime=endTime, offset=offset)))
        json_data = response.json()
        return _deserialize_withdraw_history(json_data, response)


class AsyncAccount(API):
    async def generate_listen_key(self) -> Response[str, object]:
        """Generate Listen Key

        GET openApi/user/auth/userDataStream

        https://bingx-api.github.io/docs/#/en-us/spot/socket/listenKey.html#generate%20Listen%20Key
        """
        response = validate_response(await self._async_query(**AccountCore.generate_listen_key(self)))
        json_data = response.json
        return _deserialize_listen_key(json_data, response)

    async def get_balance(self) -> Response[list[Balance], object]:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        response = validate_response(await self._async_query(**AccountCore.get_balance(self)))
        json_data = response.json
        return _deserialize_balance(json_data, response)

    async def get_deposit_address(self,
                                  asset: str,
                                  limit: int = None,
                                  offset: int = None,
                                  ) -> Response[list[DepositAddress], object]:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            limit (int, optional): Default 100; max 1000.

            offset (int, optional): Starting record number, default is 0.

        """

        response = validate_response(
            await self._async_query(**AccountCore.get_deposit_address(self, asset=asset, limit=limit, offset=offset)))
        json_data = response.json
        return _deserialize_deposit_address(json_data, response)

    async def withdraw(self,
                       asset: str,
                       address: str,
                       amount: float,
                       walletType: int,
                       network: str = None,
                       addressTag: str = None,
                       withdrawOrderId: int = None,
                       ) -> Response[Withdraw, object]:
        """Withdraw

        POST /openApi/wallets/v1/capital/withdraw/apply

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
        return _deserialize_withdraw(json_data, response)

    async def get_coins(self, asset: str = None) -> Response[list[Coin], object]:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        response = validate_response(await self._async_query(**AccountCore.get_coins(self, asset=asset)))
        json_data = response.json
        return _deserialize_coins(json_data, response)

    async def get_deposit_history(self,
                                  asset: str = None,
                                  limit: int = None,
                                  status: int = None,
                                  startTime: int = None,
                                  endTime: int = None,
                                  offset: int = None,
                                  ) -> Response[list[DepositHistory], object]:
        """Deposit History

        GET /openApi/api/v3/capital/deposit/hisrec

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Deposit%20History(supporting%20network)

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            status (int, optional): 0-In progress 6-Chain uploaded 1-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.

        """
        response = validate_response(await self._async_query(
            **AccountCore.get_deposit_history(self, asset=asset, limit=limit, status=status, startTime=startTime,
                                              endTime=endTime, offset=offset)))
        json_data = response.json
        return _deserialize_deposit_history(json_data, response)

    async def get_withdraw_history(self,
                                   id: str = None,
                                   asset: str = None,
                                   limit: int = None,
                                   withdrawOrderId: str = None,
                                   status: int = None,
                                   startTime: int = None,
                                   endTime: int = None,
                                   offset: int = None,
                                   ) -> Response[list[WithdrawHistory], object]:
        """Withdraw History

        GET /openApi/api/v3/capital/withdraw/history

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw%20History%20(supporting%20network)

        params:
            id (str, optional): Unique id of the withdrawal record returned by the platform.

            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            withdrawOrderId (str, optional): Custom ID, if there is none, this field will not be returned,When both the platform ID and withdraw order ID are passed as parameters, the query will be based on the platform ID

            status (int, optional):	4-Under Review 5-Failed 6-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.
        """
        response = validate_response(await self._async_query(
            **AccountCore.get_withdraw_history(self, id=id, asset=asset, limit=limit, withdrawOrderId=withdrawOrderId,
                                               status=status, startTime=startTime, endTime=endTime, offset=offset)))
        json_data = response.json
        return _deserialize_withdraw_history(json_data, response)


class WebSocketAccount(API):
    async def account_update(self, listenKey: str) -> Response[object, object]:
        """Subscription account balance push

        Stream Names: ACCOUNT_UPDATE

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data

        :params:
            listenKey (str): Account.generate_listen_key, (listen key Valid for 1 hour).
        """
        time_end = time.time() + 3600
        async for response in self._ws_query(**WSAccountCore.account_update(self, listenKey=listenKey)):
            if time.time() >= time_end:
                break
            json_data = json.loads(gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb').read().decode())
            if 'a' in json_data:
                yield _deserialize_account_update_for_ws(json_data, response)

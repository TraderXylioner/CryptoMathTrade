from .api import API
from ..deserialize import account as deserialize
from ..core.account import AccountCore
from ...utils import validate_response


class Account(API):
    def get_balance(self, asset: str = None):
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        response = validate_response(
            self._query(**AccountCore.get_balance(self, asset=asset))
        )
        json_data = response.json()
        return deserialize.deserialize_balance(json_data, response)

    def get_coins(self):
        """All Coins' Information

        GET /sapi/v1/capital/config/getall

        https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data
        """
        response = validate_response(self._query(**AccountCore.get_coins(self)))
        json_data = response.json()
        return deserialize.deserialize_coins(json_data, response)

    def withdraw(
        self,
        asset: str,
        address: str,
        amount: float,
        walletType: int,
        network: str = None,
        addressTag: str = None,
        withdrawOrderId: int = None,
    ):
        """Withdraw

        POST /sapi/v1/capital/withdraw/apply

        https://binance-docs.github.io/apidocs/spot/en/#enable-fast-withdraw-switch-user_data

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
        response = validate_response(
            self._query(
                **AccountCore.withdraw(
                    self,
                    asset=asset,
                    address=address,
                    amount=amount,
                    walletType=walletType,
                    network=network,
                    addressTag=addressTag,
                    withdrawOrderId=withdrawOrderId,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_withdraw(json_data, response)

    def get_deposit_history(
        self,
        asset: str = None,
        limit: int = 1000,
        status: int = None,
        startTime: int = None,
        endTime: int = None,
        offset: int = None,
        txId: str = None,
    ):
        """Deposit History

        GET /openApi/api/v3/capital/deposit/hisrec

        https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            status (int, optional): 0(0:pending,6: credited but cannot withdraw, 7=Wrong Deposit,8=Waiting User confirm, 1:success)

            startTime (int, optional): Default: 90 days from current timestamp.

            endTime (int, optional): Default: present timestamp.

            offset (int, optional): Default: 0.

            txId (str, optional).
        """
        response = validate_response(
            self._query(
                **AccountCore.get_deposit_history(
                    self,
                    asset=asset,
                    limit=limit,
                    status=status,
                    startTime=startTime,
                    endTime=endTime,
                    offset=offset,
                    txId=txId,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_deposit_history(json_data, response)

    def get_withdraw_history(
        self,
        asset: str = None,
        limit: int = 1000,
        withdrawOrderId: str = None,
        status: int = None,
        startTime: int = None,
        endTime: int = None,
        offset: int = None,
    ):
        """Withdraw History

        GET /sapi/v1/capital/withdraw/history

        https://binance-docs.github.io/apidocs/spot/en/#withdraw-history-supporting-network-user_data

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            withdrawOrderId (str, optional): Custom ID, if there is none, this field will not be returned,When both the platform ID and withdraw order ID are passed as parameters, the query will be based on the platform ID

            status (int, optional):	0(0:Email Sent,1:Cancelled 2:Awaiting Approval 3:Rejected 4:Processing 5:Failure 6:Completed)

            startTime (int, optional): Default: 90 days from current timestamp.

            endTime (int, optional): Default: present timestamp.

            offset (int, optional).
        """
        response = validate_response(
            self._query(
                **AccountCore.get_withdraw_history(
                    self,
                    asset=asset,
                    limit=limit,
                    withdrawOrderId=withdrawOrderId,
                    status=status,
                    startTime=startTime,
                    endTime=endTime,
                    offset=offset,
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_withdraw_history(json_data, response)

    def get_deposit_address(
        self,
        asset: str,
        network: str = None,
        amount: float = None,
    ):
        """Query Deposit Address

        GET /sapi/v1/capital/deposit/address

        https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data

        params:
            asset (str).

            network (str, optional). If network is not send, return with default network of the coin.

            amount (float, optional).
        """
        response = validate_response(
            self._query(
                **AccountCore.get_deposit_address(
                    self, asset=asset, network=network, amount=amount
                )
            )
        )
        json_data = response.json()
        return deserialize.deserialize_deposit_address(json_data, response)


class AsyncAccount(API):
    async def get_balance(self, asset: str = None):
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (int, optional): If asset is blank, then query all positive assets user have.
        """
        response = validate_response(
            await self._async_query(**AccountCore.get_balance(self, asset=asset))
        )
        json_data = response.json
        return deserialize.deserialize_balance(json_data, response)

    async def get_coins(self):
        """All Coins' Information

        GET /sapi/v1/capital/config/getall

        https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data
        """
        response = validate_response(
            await self._async_query(**AccountCore.get_coins(self))
        )
        json_data = response.json
        return deserialize.deserialize_coins(json_data, response)

    async def withdraw(
        self,
        asset: str,
        address: str,
        amount: float,
        walletType: int,
        network: str = None,
        addressTag: str = None,
        withdrawOrderId: int = None,
    ):
        """Withdraw

        POST /sapi/v1/capital/withdraw/apply

        https://binance-docs.github.io/apidocs/spot/en/#enable-fast-withdraw-switch-user_data

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
        response = validate_response(
            await self._async_query(
                **AccountCore.withdraw(
                    self,
                    asset=asset,
                    address=address,
                    amount=amount,
                    walletType=walletType,
                    network=network,
                    addressTag=addressTag,
                    withdrawOrderId=withdrawOrderId,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_withdraw(json_data, response)

    async def get_deposit_history(
        self,
        asset: str = None,
        limit: int = 1000,
        status: int = None,
        startTime: int = None,
        endTime: int = None,
        offset: int = None,
        txId: str = None,
    ):
        """Deposit History

        GET /openApi/api/v3/capital/deposit/hisrec

        https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            status (int, optional): 0(0:pending,6: credited but cannot withdraw, 7=Wrong Deposit,8=Waiting User confirm, 1:success)

            startTime (int, optional): Default: 90 days from current timestamp.

            endTime (int, optional): Default: present timestamp.

            offset (int, optional): Default: 0.

            txId (str, optional).
        """
        response = validate_response(
            await self._async_query(
                **AccountCore.get_deposit_history(
                    self,
                    asset=asset,
                    limit=limit,
                    status=status,
                    startTime=startTime,
                    endTime=endTime,
                    offset=offset,
                    txId=txId,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_deposit_history(json_data, response)

    async def get_withdraw_history(
        self,
        asset: str = None,
        limit: int = 1000,
        withdrawOrderId: str = None,
        status: int = None,
        startTime: int = None,
        endTime: int = None,
        offset: int = None,
    ):
        """Withdraw History

        GET /sapi/v1/capital/withdraw/history

        https://binance-docs.github.io/apidocs/spot/en/#withdraw-history-supporting-network-user_data

        params:
            asset (str, optional).

            limit (int, optional): Default 1000; max 1000.

            withdrawOrderId (str, optional): Custom ID, if there is none, this field will not be returned,When both the platform ID and withdraw order ID are passed as parameters, the query will be based on the platform ID

            status (int, optional):	0(0:Email Sent,1:Cancelled 2:Awaiting Approval 3:Rejected 4:Processing 5:Failure 6:Completed)

            startTime (int, optional): Default: 90 days from current timestamp.

            endTime (int, optional): Default: present timestamp.

            offset (int, optional).
        """
        response = validate_response(
            await self._async_query(
                **AccountCore.get_withdraw_history(
                    self,
                    asset=asset,
                    limit=limit,
                    withdrawOrderId=withdrawOrderId,
                    status=status,
                    startTime=startTime,
                    endTime=endTime,
                    offset=offset,
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_withdraw_history(json_data, response)

    async def get_deposit_address(
        self,
        asset: str,
        network: str = None,
        amount: float = None,
    ):
        """Query Deposit Address

        GET /sapi/v1/capital/deposit/address

        https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data

        params:
            asset (str).

            network (str, optional). If network is not send, return with default network of the coin.

            amount (float, optional).
        """
        response = validate_response(
            await self._async_query(
                **AccountCore.get_deposit_address(
                    self, asset=asset, network=network, amount=amount
                )
            )
        )
        json_data = response.json
        return deserialize.deserialize_deposit_address(json_data, response)


# TODO: WebSocketAccount

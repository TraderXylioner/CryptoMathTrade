from ..api.api import API
from ..urls import URLS
from ...utils import get_timestamp, replace_param, check_require_params


class AccountCore(API):
    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /sapi/v1/capital/config/getall

        https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data
        """
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_COINS_URL,
            params=self.get_payload(params),
        )

    def get_balance(self, **params) -> dict:
        """Query Assets

        POST /sapi/v3/asset/getUserAsset

        https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data

        params:
            asset (str, optional): If asset is blank, then query all positive assets user have.
        """
        return self.return_args(
            method="POST",
            url=URLS.BASE_URL + URLS.GET_BALANCE_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("asset",))
    def get_deposit_address(self, **params) -> dict:
        """Query Deposit Address

        GET /sapi/v1/capital/deposit/address

        https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data

        params:
            asset (str).

            network (str, optional). If network is not send, return with default network of the coin.

            amount (float, optional).
        """
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_DEPOSIT_ADDRESS_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("asset", "address", "amount"))
    def withdraw(self, **params) -> dict:
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
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="POST",
            url=URLS.BASE_URL + URLS.WITHDRAW_URL,
            params=self.get_payload(params),
        )

    def get_deposit_history(self, **params) -> dict:
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
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_DEPOSIT_HISTORY,
            params=self.get_payload(params),
        )

    def get_withdraw_history(self, **params) -> dict:
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
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_WITHDRAW_HISTORY,
            params=self.get_payload(params),
        )


# TODO: WSAccountCore

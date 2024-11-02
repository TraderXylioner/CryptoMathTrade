from ..api.api import API
from ..urls import URLS
from ...utils import replace_param, get_timestamp, check_require_params


class AccountCore(API):
    def generate_listen_key(self, **params) -> dict:
        """Generate Listen Key

        GET openApi/user/auth/userDataStream

        https://bingx-api.github.io/docs/#/en-us/spot/socket/listenKey.html#generate%20Listen%20Key
        """
        return self.return_args(
            method="POST",
            url=URLS.BASE_URL + URLS.LISTEN_KEY,
            params=self.get_payload(params),
        )

    def get_balance(self, **params) -> dict:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_BALANCE_URL,
            params=self.get_payload(params),
        )

    @check_require_params(("asset",))
    def get_deposit_address(self, **params) -> dict:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            limit (int, optional): Default 100; max 1000.

            offset (int): Starting record number, default is 0.
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

        POST /openApi/wallets/v1/capital/withdraw/apply

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            address (str).

            amount (float).

            !  transactionFeeFlag (bool, optional): When making internal transfer, true for returning the fee to the destination account; false for returning the fee back to the departure account. Default false.

            !  name (str): Description of the address. The upper limit of the address book is 200. Exceeding the limit will cause withdrawal failure. Space in name should be encoded into %20.

            walletType (int): The wallet type for withdraw，0-spot wallet ，1-funding wallet. Default walletType is the current "selected wallet" under wallet->Fiat and Spot/Funding->Deposit

            network (str, optional).

            addressTag (str, optional): Secondary address identifier for coins like XRP,XMR etc.

            withdrawOrderId (str, optional): client id for withdraw
        """
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="POST",
            url=URLS.BASE_URL + URLS.WITHDRAW_URL,
            params=self.get_payload(params),
        )

    def get_coins(self, **params) -> dict:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_COINS_URL,
            params=self.get_payload(params),
        )

    def get_deposit_history(self, **params) -> dict:
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
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_DEPOSIT_HISTORY,
            params=self.get_payload(params),
        )

    def get_withdraw_history(self, **params) -> dict:
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
        replace_param(params, "asset", "coin")
        params["timestamp"] = get_timestamp()
        return self.return_args(
            method="GET",
            url=URLS.BASE_URL + URLS.GET_WITHDRAW_HISTORY,
            params=self.get_payload(params),
        )


class WSAccountCore(API):
    @check_require_params(("listenKey",))
    def account_update(self, **params) -> dict:
        """Subscription account balance push

        Stream Names: ACCOUNT_UPDATE

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data

        :params:
            listenKey (str): Account.generate_listen_key, (listen key Valid for 1 hour).
        """
        return self.return_args(
            method="sub",
            url=f'{URLS.WS_BASE_URL}?listenKey={params["listenKey"]}',
            params="ACCOUNT_UPDATE",
        )

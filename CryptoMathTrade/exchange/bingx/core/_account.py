from .._api import API
from .._urls import URLS
from ...utils import replace_param, get_timestamp


class AccountCore(API):
    def generate_listen_key(self, **kwargs) -> dict:
        """Generate Listen Key

        GET openApi/user/auth/userDataStream

        https://bingx-api.github.io/docs/#/en-us/spot/socket/listenKey.html#generate%20Listen%20Key
        """
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.LISTEN_KEY, params=self.get_payload(kwargs))

    def get_balance(self, **kwargs) -> dict:
        """Query Assets

        GET /openApi/spot/v1/account/balance

        https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
        """
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_BALANCE_URL, params=self.get_payload(kwargs))

    def get_deposit_address(self, **kwargs) -> dict:
        """Query Deposit Address

        GET /openApi/wallets/v1/capital/deposit/address

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw

        params:
            asset (str).

            offset (int): Starting record number, default is 0.

            limit (int, optional): Default 100; max 1000.
        """
        replace_param(kwargs, 'asset', 'coin')
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='GET',
                                url=URLS.BASE_URL + URLS.GET_DEPOSIT_ADDRESS_URL,
                                params=self.get_payload(kwargs),
                                )

    def withdraw(self, **kwargs) -> dict:
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
        replace_param(kwargs, 'asset', 'coin')
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='POST', url=URLS.BASE_URL + URLS.WITHDRAW_URL, params=self.get_payload(kwargs))

    def get_coins(self, **kwargs) -> dict:
        """All Coins' Information

        GET /openApi/wallets/v1/capital/config/getall

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information

        params:
            asset (str, optional).
        """
        replace_param(kwargs, 'asset', 'coin')
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_COINS_URL, params=self.get_payload(kwargs))

    def get_deposit_history(self, **kwargs) -> dict:
        """Deposit History

        GET /openApi/api/v3/capital/deposit/hisrec

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Deposit%20History(supporting%20network)

        params:
            asset (str, optional).

            status (int, optional): 0-In progress 6-Chain uploaded 1-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.

            limit (int, optional): Default 1000; max 1000.
        """
        replace_param(kwargs, 'asset', 'coin')
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_DEPOSIT_HISTORY,
                                params=self.get_payload(kwargs))

    def get_withdraw_history(self, **kwargs) -> dict:
        """Withdraw History

        GET /openApi/api/v3/capital/withdraw/history

        https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw%20History%20(supporting%20network)

        params:
            id (str, optional): Unique id of the withdrawal record returned by the platform.

            asset (str, optional).

            withdrawOrderId (str, optional): Custom ID, if there is none, this field will not be returned,When both the platform ID and withdraw order ID are passed as parameters, the query will be based on the platform ID

            status (int, optional):	4-Under Review 5-Failed 6-Completed.

            startTime (int, optional).

            endTime (int, optional).

            offset (int, optional): Default: 0.

            limit (int, optional): Default 1000; max 1000.
        """
        replace_param(kwargs, 'asset', 'coin')
        kwargs['timestamp'] = get_timestamp()
        return self.return_args(method='GET', url=URLS.BASE_URL + URLS.GET_WITHDRAW_HISTORY,
                                params=self.get_payload(kwargs))


class WSAccountCore(API):
    def account_update(self, **kwargs) -> dict:
        """Subscription account balance push

        Stream Names: ACCOUNT_UPDATE

        https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data

        :params:
            listenKey (str): Account.generate_listen_key, (listen key Valid for 1 hour).
        """
        return self.return_args(method='sub',
                                url=f'{URLS.WS_BASE_URL}?listenKey={kwargs["listenKey"]}',
                                params='ACCOUNT_UPDATE')

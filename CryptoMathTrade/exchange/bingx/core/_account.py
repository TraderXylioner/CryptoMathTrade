from .._api import API
from .._urls import URLS
from ...utils import replace_param, get_timestamp


class AccountCore(API):
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

#  TODO: deposit history, withdraw history

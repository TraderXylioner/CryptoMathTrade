from decimal import Decimal

from pydantic import BaseModel


class Balance(BaseModel):
    asset: str
    free: float
    locked: float


class WithdrawHistory(BaseModel):
    id: str
    amount: Decimal
    coin: str
    network: str
    status: int
    address: str
    sourceAddress: str = None
    transferType: int
    transactionFee: str
    confirmNo: int
    info: str
    txId: str
    applyTime: str


class DepositHistory(BaseModel):
    id: str = None
    amount: Decimal
    coin: str
    network: str
    status: int
    address: str
    addressTag: str = None
    sourceAddress: str = None
    txId: str
    insertTime: int
    unlockConfirm: str | int
    confirmTimes: str


class DepositAddress(BaseModel):
    coinId: int = None
    coin: str
    address: str
    network: str = None
    url: str = None
    isDefault: int = None
    tag: str = None


class Coin(BaseModel):
    coin: str
    name: str
    networkList: list
    isLegalMoney: bool = None
    trading: bool = None


class Withdraw(BaseModel):
    id: str

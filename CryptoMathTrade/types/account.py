from decimal import Decimal

from pydantic import BaseModel


class Balance(BaseModel):
    asset: str
    free: float
    locked: float


class WithdrawHistory(BaseModel):
    amount: Decimal
    coin: str
    network: str
    status: int
    address: str
    sourceAddress: str
    txIdtxId: str
    insertTime: int
    unlockConfirm: str
    confirmTimes: str


class DepositHistory(BaseModel):
    amount: Decimal
    coin: str
    network: str
    status: int
    address: str
    sourceAddress: str
    txIdtxId: str
    insertTime: int
    unlockConfirm: str
    confirmTimes: str


class DepositAddress(BaseModel):
    coinId: int
    coin: str
    network: str
    address: str
    tag: str


class Coin(BaseModel):
    coin: str
    name: str
    networkList: list


class Withdraw(BaseModel):
    id: str

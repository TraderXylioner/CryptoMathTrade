from pydantic import BaseModel


class Balance(BaseModel):
    asset: str
    free: float
    locked: float
    # freeze: float
    # withdrawing: float
    # ipoable: float
    # btcValuation: float

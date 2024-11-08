from pydantic import BaseModel


class Ticker(BaseModel):
    id: int | None = None
    symbol: str
    firstCoin: str | None = None
    secondCoin: str | None = None
    openPrice: float | None = None
    highPrice: float
    lowPrice: float
    lastPrice: float
    volume: float
    quoteVolume: float | None = None
    closeTime: int | None = None

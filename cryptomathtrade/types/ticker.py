from pydantic import BaseModel


class Ticker(BaseModel):
    id: int | None = None
    symbol: str
    firstCoin: str | None = None
    secondCoin: str | None = None
    openPrice: float | None = None
    highPrice: float | None = None
    lowPrice: float | None = None
    lastPrice: float
    volume: float
    volumeQuote: float | None = None
    closeTime: int | None = None

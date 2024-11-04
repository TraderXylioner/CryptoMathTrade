from pydantic import BaseModel


class Ticker(BaseModel):
    id: int | None = None
    symbol: str
    openPrice: float | None = None
    highPrice: float
    lowPrice: float
    lastPrice: float
    volume: float
    quoteVolume: float
    closeTime: int

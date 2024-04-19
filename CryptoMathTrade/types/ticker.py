from pydantic import BaseModel


class Ticker(BaseModel):
    symbol: str
    openPrice: float
    highPrice: float
    lowPrice: float
    lastPrice: float
    volume: float
    quoteVolume: float
    closeTime: int

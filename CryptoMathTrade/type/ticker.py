from dataclasses import dataclass


@dataclass
class Ticker:
    symbol: str
    priceChange: float
    priceChangePercent: float
    openPrice: float
    highPrice: float
    lowPrice: float
    lastPrice: float
    volume: float
    quoteVolume: float
    closeTime: int
    openTime: int | None = None
    weightedAvgPrice: float | None = None
    firstId: int | None = None
    lastId: int | None = None
    count: int | None = None

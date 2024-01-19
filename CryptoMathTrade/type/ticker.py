from dataclasses import dataclass


@dataclass
class Ticker:
    symbol: str
    priceChange: float
    priceChangePercent: float
    weightedAvgPrice: float
    openPrice: float
    highPrice: float
    lowPrice: float
    lastPrice: float
    volume: float
    quoteVolume: float
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int

class URLS:
    # HTTP
    BASE_URL = "https://api.kucoin.com"

    # Market
    DEPTH_URL = "/api/v1/market/orderbook/level2_100"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-part-order-book-aggregated-
    TRADES_URL = "/api/v1/market/histories"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-trade-histories
    TICKER_URL = "/api/v1/market/stats"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-24hr-stats
    TICKERS_URL = "/api/v1/market/allTickers"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-all-tickers
    SYMBOLS_URL = "/api/v2/symbols"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-symbols-list
    KLINE_URL = "/api/v1/market/candles"  # https://www.kucoin.com/docs/rest/spot-trading/market-data/get-klines

    # WS
    WS_BASE_URL = "wss://ws-api-spot.kucoin.com/"

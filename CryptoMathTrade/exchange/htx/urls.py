class URLS:
    # HTTP
    BASE_URL = "https://api.huobi.pro"

    # Market
    DEPTH_URL = (
        "/market/depth"  # https://huobiapi.github.io/docs/spot/v1/en/#get-market-depth
    )
    TRADES_URL = "/market/history/trade"  # https://huobiapi.github.io/docs/spot/v1/en/#get-the-most-recent-trades
    TICKER_URL = "/market/detail/merged"  # https://huobiapi.github.io/docs/spot/v1/en/#get-latest-aggregated-ticker
    TICKERS_URL = "/market/tickers"  # https://huobiapi.github.io/docs/spot/v1/en/#get-latest-tickers-for-all-pairs
    SYMBOLS_URL = "/v2/settings/common/symbols"  # https://huobiapi.github.io/docs/spot/v1/en/#get-all-supported-trading-symbol-v2
    KLINE_URL = "/market/history/kline"  # https://huobiapi.github.io/docs/spot/v1/en/#get-klines-candles

    # WS
    WS_BASE_URL = "wss://api.huobi.pro/ws"

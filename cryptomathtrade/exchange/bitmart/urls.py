class URLS:
    # HTTP
    BASE_URL = "https://api-cloud.bitmart.com"

    # Market
    DEPTH_URL = "/spot/quotation/v3/books"  # https://developer-pro.bitmart.com/en/spot/#get-depth-v3
    TRADES_URL = "/spot/quotation/v3/trades"  # https://developer-pro.bitmart.com/en/spot/#get-recent-trades-v3
    TICKER_URL = "/spot/quotation/v3/ticker"  # https://developer-pro.bitmart.com/en/spot/#get-ticker-of-a-trading-pair-v3
    TICKERS_URL = "/spot/quotation/v3/tickers"  # https://developer-pro.bitmart.com/en/spot/#get-ticker-of-all-pairs-v3
    SYMBOLS_URL = "/spot/v1/symbols/details"  # https://developer-pro.bitmart.com/en/spot/#get-trading-pair-details-v1
    KLINE_URL = "/spot/quotation/v3/klines"  # https://developer-pro.bitmart.com/en/spot/#get-history-k-line-v3

    # WS
    WS_BASE_URL = "wss://ws-manager-compress.bitmart.com/api?protocol=1.1"

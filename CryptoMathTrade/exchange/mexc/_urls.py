class URLS:
    # HTTP
    BASE_URL = 'https://api.mexc.com'
    BASE2_URL = 'https://www.mexc.com'

    # Market
    DEPTH_URL = '/api/v3/depth'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book
    TRADES_URL = '/api/v3/trades'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list
    TICKER_URL = '/api/v3/ticker/24hr'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics
    SYMBOLS_URL = '/open/api/v2/market/symbols'  # https://mexcdevelop.github.io/apidocs/spot_v2_en/#all-symbols
    KLINE_URL = '/api/v3/klines'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#kline-candlestick-data

    # Account
    GET_BALANCE = '/api/v3/account'

    # WS
    WS_BASE_URL = 'wss://wbs.mexc.com/ws'

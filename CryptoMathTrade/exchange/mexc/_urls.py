class URLS:
    # HTTP
    BASE_URL = 'https://api.mexc.com'

    # Market
    DEPTH_URL = '/api/v3/depth'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#order-book
    TRADES_URL = '/api/v3/trades'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#recent-trades-list
    TICKER_URL = '/api/v3/ticker/24hr'  # https://mexcdevelop.github.io/apidocs/spot_v3_en/#24hr-ticker-price-change-statistics

    # WS
    WS_BASE_URL = 'wss://wbs.mexc.com/ws'

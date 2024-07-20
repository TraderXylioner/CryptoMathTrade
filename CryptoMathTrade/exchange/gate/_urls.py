class URLS:
    # HTTP
    BASE_URL = 'https://api.gateio.ws'

    # Market
    DEPTH_URL = '/api/v4/spot/order_book'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book
    TRADES_URL = '/api/v4/spot/trades'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades
    TICKER_URL = '/api/v4/spot/tickers'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information
    SYMBOLS_URL = '/api/v4/spot/currency_pairs'  # https://www.gate.io/docs/developers/apiv4/en/#list-all-currency-pairs-supported
    KLINE_URL = '/api/v4/spot/candlesticks'  # https://www.gate.io/docs/developers/apiv4/en/#market-candlesticks

    # Account
    GET_BALANCE = '/api/v4/spot/accounts'

    # WS
    WS_BASE_URL = 'wss://api.gateio.ws/ws/v4/'

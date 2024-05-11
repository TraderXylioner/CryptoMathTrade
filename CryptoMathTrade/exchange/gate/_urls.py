class URLS:
    # HTTP
    BASE_URL = 'https://api.gateio.ws'

    # Market
    DEPTH_URL = '/api/v4/spot/order_book'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-order-book
    TRADES_URL = '/api/v4/spot/trades'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-market-trades
    TICKER_URL = '/api/v4/spot/tickers'  # https://www.gate.io/docs/developers/apiv4/en/#retrieve-ticker-information

    # WS
    WS_BASE_URL = 'wss://api.gateio.ws/ws/v4/'

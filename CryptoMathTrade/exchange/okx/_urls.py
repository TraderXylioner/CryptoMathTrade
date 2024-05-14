class URLS:
    # HTTP
    BASE_URL = 'https://www.okx.com'

    # Market
    DEPTH_URL = '/api/v5/market/books'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book
    TRADES_URL = '/api/v5/market/trades'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades
    TICKER_URL = '/api/v5/market/ticker'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
    TICKERS_URL = '/api/v5/market/tickers'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers

    # WS
    WS_BASE_URL = 'wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999'

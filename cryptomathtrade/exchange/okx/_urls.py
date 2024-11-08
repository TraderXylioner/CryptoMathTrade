class URLS:
    # HTTP
    BASE_URL = 'https://www.okx.com'

    # Market
    DEPTH_URL = '/api/v5/market/books'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-order-book
    TRADES_URL = '/api/v5/market/trades'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-trades
    TICKER_URL = '/api/v5/market/ticker'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-ticker
    TICKERS_URL = '/api/v5/market/tickers'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers
    SYMBOLS_URL = '/api/v5/public/instruments'  # https://www.okx.com/docs-v5/en/#public-data-rest-api-get-instruments
    KLINE_URL = '/api/v5/market/history-candles'  # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-candlesticks-history

    # Account
    GET_BALANCE = '/api/v5/account/balance'

    # WS
    WS_BASE_URL = 'wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999'

class URLS:
    # HTTP
    BASE_URL = 'https://api.bitget.com'
    DEPTH_URL = '/api/v2/spot/market/orderbook'
    TRADES_URL = '/api/v2/spot/market/fills'
    TICKER_URL = '/api/v2/spot/market/tickers'
    SYMBOLS_URL = '/api/v2/spot/public/symbols'
    KLINE_URL = '/api/v2/spot/market/candles'

    GET_BALANCE = '/api/v2/spot/account/assets'

    # WS
    WS_BASE_URL = 'wss://ws.bitget.com/v2/ws/public'

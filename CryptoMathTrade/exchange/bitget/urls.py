class URLS:
    # HTTP
    BASE_URL = "https://api.bitget.com"

    # MARKET
    DEPTH_URL = "/api/v2/spot/market/orderbook"  # https://www.bitget.com/api-doc/spot/market/Get-Orderbook
    TRADES_URL = "/api/v2/spot/market/fills"  # https://www.bitget.com/api-doc/spot/market/Get-Recent-Trades
    TICKER_URL = "/api/v2/spot/market/tickers"  # https://www.bitget.com/api-doc/spot/market/Get-Tickers
    SYMBOLS_URL = "/api/v2/spot/public/symbols"  # https://www.bitget.com/api-doc/spot/market/Get-Symbols
    KLINE_URL = "/api/v2/spot/market/candles"  # https://www.bitget.com/api-doc/spot/market/Get-Candle-Data

    # WS
    WS_BASE_URL = "wss://ws.bitget.com/v2/ws/public"  # https://www.bitget.com/api-doc/spot/websocket/public/Depth-Channel

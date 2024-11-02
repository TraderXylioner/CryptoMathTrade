class URLS:
    # HTTP
    BASE_URL = "https://api.binance.com"

    # Market

    DEPTH_URL = "/api/v3/depth"  # https://binance-docs.github.io/apidocs/spot/en/#order-book
    TRADES_URL = "/api/v3/trades"  # https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list
    TICKER_URL = "/api/v3/ticker/24hr"  # https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics
    KLINE_URL = "/api/v3/klines"  # https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data
    SYMBOLS_URL = "/api/v3/exchangeInfo"  # https://binance-docs.github.io/apidocs/spot/en/#exchange-information

    # Spot
    ORDER_URL = "/api/v3/order"  # https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data
    CREATE_ORDER_URL = "/api/v3/order"  # https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
    CANCEL_ORDER_URL = "/api/v3/order"  # https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade

    GET_ORDERS_URL = "/api/v3/allOrders"  # https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data
    OPEN_ORDERS_URL = "/api/v3/openOrders"  # https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data
    CANCEL_ORDERS_URL = "/api/v3/openOrders"  # https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade

    # Account
    GET_BALANCE_URL = "/sapi/v3/asset/getUserAsset"  # https://binance-docs.github.io/apidocs/spot/en/#user-asset-user_data
    GET_COINS_URL = "/sapi/v1/capital/config/getall"  # https://binance-docs.github.io/apidocs/spot/en/#all-coins-39-information-user_data
    GET_DEPOSIT_HISTORY = "/sapi/v1/capital/deposit/hisrec"  # https://binance-docs.github.io/apidocs/spot/en/#deposit-history-supporting-network-user_data
    GET_WITHDRAW_HISTORY = "/sapi/v1/capital/withdraw/history"  # https://binance-docs.github.io/apidocs/spot/en/#withdraw-history-supporting-network-user_data
    GET_DEPOSIT_ADDRESS_URL = "/sapi/v1/capital/deposit/address"  # https://binance-docs.github.io/apidocs/spot/en/#deposit-address-supporting-network-user_data
    WITHDRAW_URL = "/sapi/v1/capital/withdraw/apply"  # https://binance-docs.github.io/apidocs/spot/en/#enable-fast-withdraw-switch-user_data

    # WS
    WS_BASE_URL = "wss://stream.binance.com:443/ws"

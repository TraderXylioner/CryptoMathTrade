class URLS:
    # HTTP
    BASE_URL = 'https://api.binance.com'
    DEPTH_URL = '/api/v3/depth'  # https://binance-docs.github.io/apidocs/spot/en/#order-book
    TRADES_URL = '/api/v3/trades'  # https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list
    TICKER_URL = '/api/v3/ticker'  # https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics

    ORDER_URL = '/api/v3/order'  # https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data or
    # https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade or
    # https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
    GET_ORDERS_URL = '/api/v3/allOrders'  # https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data
    OPEN_ORDERS_URL = '/api/v3/openOrders'  # https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data

    GET_DEPOSIT_ADDRESS = '/sapi/v1/capital/deposit/address'

    # WS
    WS_BASE_URL = 'wss://stream.binance.com:9443/ws'

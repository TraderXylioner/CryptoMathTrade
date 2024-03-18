class URLS:
    # HTTP
    BASE_URL = 'https://open-api.bingx.com'
    DEPTH_URL = '/openApi/spot/v1/market/depth'
    TRADES_URL = '/openApi/spot/v1/market/trades'
    TICKER_URL = '/openApi/spot/v1/ticker/24hr'

    ORDER_URL = '/openApi/spot/v1/trade/query'
    CREATE_ORDER_URL = '/openApi/spot/v1/trade/order'
    GET_ORDERS_URL = '/openApi/spot/v1/trade/historyOrders'
    OPEN_ORDERS_URL = '/openApi/spot/v1/trade/openOrders'
    CANCEL_ORDER_URL = '/openApi/spot/v1/trade/cancel'
    CANCEL_ORDERS_URL = '/openApi/spot/v1/trade/cancelOpenOrders'

    # GET_DEPOSIT_ADDRESS = '/sapi/v1/capital/deposit/address'

    # WS
    WS_BASE_URL = 'wss://open-api-ws.bingx.com/market'

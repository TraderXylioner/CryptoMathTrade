class URLS:
    # HTTP
    BASE_URL = 'https://open-api.bingx.com'
    DEPTH_URL = '/openApi/spot/v1/market/depth'
    TRADES_URL = '/openApi/spot/v1/market/trades'
    TICKER_URL = '/openApi/spot/v1/ticker/24hr'

    # ORDER_URL = '/api/v3/order'
    GET_ORDERS_URL = '/openApi/spot/v1/trade/query'
    # OPEN_ORDERS_URL = '/api/v3/openOrders'

    # GET_DEPOSIT_ADDRESS = '/sapi/v1/capital/deposit/address'

    # WS
    WS_BASE_URL = 'wss://open-api-ws.bingx.com/market'

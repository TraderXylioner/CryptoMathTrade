class URLS:
    # HTTP
    BASE_URL = 'https://open-api.bingx.com'
    DEPTH_URL = '/openApi/spot/v1/market/depth'
    TRADES_URL = '/openApi/spot/v1/market/trades'
    TICKER_URL = '/openApi/spot/v1/ticker/24hr'
    SYMBOLS_URL = '/openApi/spot/v1/common/symbols'
    KLINE_URL = '/openApi/market/his/v1/kline'

    ORDER_URL = '/openApi/spot/v1/trade/query'
    CREATE_ORDER_URL = '/openApi/spot/v1/trade/order'
    CANCEL_ORDER_URL = '/openApi/spot/v1/trade/cancel'

    GET_ORDERS_URL = '/openApi/spot/v1/trade/historyOrders'
    OPEN_ORDERS_URL = '/openApi/spot/v1/trade/openOrders'
    CANCEL_ORDERS_URL = '/openApi/spot/v1/trade/cancelOpenOrders'

    GET_BALANCE_URL = '/openApi/spot/v1/account/balance'
    GET_DEPOSIT_ADDRESS_URL = '/openApi/wallets/v1/capital/deposit/address'
    WITHDRAW_URL = '/openApi/wallets/v1/capital/withdraw/apply'
    GET_COINS_URL = '/openApi/wallets/v1/capital/config/getall'

    # WS
    WS_BASE_URL = 'wss://open-api-ws.bingx.com/market'

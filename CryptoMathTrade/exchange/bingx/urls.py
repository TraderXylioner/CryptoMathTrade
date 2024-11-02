class URLS:
    # HTTP
    BASE_URL = "https://open-api.bingx.com"

    # MARKET
    DEPTH_URL = "/openApi/spot/v1/market/depth"  # https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20depth%20information
    TRADES_URL = "/openApi/spot/v1/market/trades"  # https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20transaction%20records
    TICKER_URL = "/openApi/spot/v1/ticker/24hr"  # https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#24-hour%20price%20changes
    SYMBOLS_URL = "/openApi/spot/v1/common/symbols"  # https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Query%20Symbols
    KLINE_URL = "/openApi/market/his/v1/kline"  # https://bingx-api.github.io/docs/#/en-us/spot/market-api.html#Historical%20K-line%20data

    # SPOT
    ORDER_URL = "/openApi/spot/v1/trade/query"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Orders
    CREATE_ORDER_URL = "/openApi/spot/v1/trade/order"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Create%20an%20Order
    CANCEL_ORDER_URL = "/openApi/spot/v1/trade/cancel"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20an%20Order
    GET_ORDERS_URL = "/openApi/spot/v1/trade/historyOrders"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Order%20History
    OPEN_ORDERS_URL = "/openApi/spot/v1/trade/openOrders"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Query%20Open%20Orders
    CANCEL_ORDERS_URL = "/openApi/spot/v1/trade/cancelOpenOrders"  # https://bingx-api.github.io/docs/#/en-us/spot/trade-api.html#Cancel%20orders%20by%20symbol

    # ACCOUNT
    GET_BALANCE_URL = "/openApi/spot/v1/account/balance"  # https://bingx-api.github.io/docs/#/en-us/common/account-api.html#Query%20Assets
    GET_DEPOSIT_ADDRESS_URL = "/openApi/wallets/v1/capital/deposit/address"  # https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Main%20Account%20Deposit%20Address
    WITHDRAW_URL = "/openApi/wallets/v1/capital/withdraw/apply"  # https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw
    GET_COINS_URL = "/openApi/wallets/v1/capital/config/getall"  # https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#All%20Coins'%20Information
    GET_DEPOSIT_HISTORY = "/openApi/api/v3/capital/deposit/hisrec"  # https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Deposit%20History(supporting%20network)
    GET_WITHDRAW_HISTORY = "/openApi/api/v3/capital/withdraw/history"  # https://bingx-api.github.io/docs/#/en-us/common/wallet-api.html#Withdraw%20History%20(supporting%20network)

    # WS
    WS_BASE_URL = "wss://open-api-ws.bingx.com/market"  # https://bingx-api.github.io/docs/#/en-us/spot/socket/account.html#Subscription%20order%20update%20data
    LISTEN_KEY = "/openApi/user/auth/userDataStream"  # https://bingx-api.github.io/docs/#/en-us/spot/socket/listenKey.html#generate%20Listen%20Key

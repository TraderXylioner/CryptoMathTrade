import requests

from CryptoMathTrade.exchange import ExchangeCores


print(ExchangeCores.get_core('kucoin').get_depth_args(symbol='BTCUSDT'))

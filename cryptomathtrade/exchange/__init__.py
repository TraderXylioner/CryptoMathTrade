from . import binance
from . import bingx
from . import bybit
from . import kucoin
from . import okx
from . import htx
from . import bitmart
from . import gate
from . import mexc
from . import bitget
from . import ascendex
from . import lbank


Exchanges = {
    "binance": binance,
    "bingx": bingx,
    "bybit": bybit,
    "kucoin": kucoin,
    "okx": okx,
    "htx": htx,
    "bitmart": bitmart,
    "gate": gate,
    "mexc": mexc,
    "bitget": bitget,
    "ascendex": ascendex,
}


def get_exchange(exchange_name):
    """
    Get the module object for a specific exchange.

    Args:
        exchange_name (str): Name of the exchange.

    Returns:
        Module: Module object for the specified exchange.
    """
    return Exchanges.get(exchange_name)

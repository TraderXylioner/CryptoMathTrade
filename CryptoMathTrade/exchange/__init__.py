from .binance import core as binanceCore
from .kucoin import core as kucoinCore
from .okx import core as okxCore
from .htx import core as htxCore
from .bitmart import core as bitmartCore
from .gate import core as gateCore
from .mexc import core as mexcCore
from .bitget import core as bitgetCore
from .ascendex import core as ascendexCore


class ExchangeCores:
    """
    Class representing cores of different exchanges.
    """
    cores = {
        'binance': binanceCore,
        'kucoin': kucoinCore,
        'okx': okxCore,
        'htx': htxCore,
        'bitmart': bitmartCore,
        'gate': gateCore,
        'mexc': mexcCore,
        'bitget': bitgetCore,
        'ascendex': ascendexCore,
    }

    @classmethod
    def get_core(cls, exchange_name):
        """
        Get the core object for a specific exchange.

        Args:
            exchange_name (str): Name of the exchange.

        Returns:
            Core: Core object for the specified exchange.
        """
        return cls.cores.get(exchange_name)

from .binance.core import Core as binanceCore
from .kucoin.core import Core as kucoinCore
from .okx.core import Core as okxCore
from .htx.core import Core as htxCore
from .bitmart.core import Core as bitmartCore
from .gate.core import Core as gateCore
from .mexc.core import Core as mexcCore
from .bitget.core import Core as bitgetCore
from .ascendex.core import Core as ascendexCore


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

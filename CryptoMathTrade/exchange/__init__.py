from .binance.core import Core as binance_core
from .kucoin.core import Core as kucoin_core
from .okx.core import Core as okx_core


class ExchangeCores:
    """
    Class representing cores of different exchanges.
    """
    cores = {
        'binance': binance_core,
        'kucoin': kucoin_core,
        'okx': okx_core,
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

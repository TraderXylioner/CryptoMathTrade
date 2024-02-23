from .binance.core import Core as binance_core
from .kucoin.core import Core as kucoin_core
from .okx.core import Core as okx_core
from .htx.core import Core as htx_core
from .bitmart.core import Core as bitmart_core
from .gate.core import Core as gate_core
from .mexc.core import Core as mexc_core
from .bitget.core import Core as bitget_core
from .ascendex.core import Core as ascendex_core


class ExchangeCores:
    """
    Class representing cores of different exchanges.
    """
    cores = {
        'binance': binance_core,
        'kucoin': kucoin_core,
        'okx': okx_core,
        'htx': htx_core,
        'bitmart': bitmart_core,
        'gate': gate_core,
        'mexc': mexc_core,
        'bitget': bitget_core,
        'ascendex': ascendex_core,
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

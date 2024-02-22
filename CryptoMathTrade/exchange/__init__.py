from .binance.core import Core as binance_core


class ExchangeCores:
    """
    Class representing cores of different exchanges.
    """
    cores = {
        'binance': binance_core(),
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

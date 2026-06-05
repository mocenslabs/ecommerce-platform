from abc import (
    ABC,
    abstractmethod,
)


class BasePaymentProvider(ABC):
    """
    Abstract base class for payment providers.

    Every payment gateway integration should inherit
    from this class to maintain a unified interface.
    """

    @abstractmethod
    def create_payment(self, payment):
        """
        Create payment in external provider.
        """
        pass

    @abstractmethod
    def refund_payment(self, payment):
        """
        Refund external payment.
        """
        pass

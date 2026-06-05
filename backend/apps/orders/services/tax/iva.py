from decimal import Decimal

from apps.orders.services.tax.base import (
    BaseTaxStrategy,
)


class ArgentinaIVAStrategy(
    BaseTaxStrategy,
):
    """
    Argentina IVA strategy.
    """

    IVA_RATE = Decimal("0.21")

    def calculate(
        self,
        order,
    ):
        return (order.subtotal_amount * self.IVA_RATE).quantize(Decimal("0.01"))

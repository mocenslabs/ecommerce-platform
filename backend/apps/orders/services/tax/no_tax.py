from decimal import Decimal

from apps.orders.services.tax.base import (
    BaseTaxStrategy,
)


class NoTaxStrategy(
    BaseTaxStrategy,
):
    """
    No tax strategy.
    """

    def calculate(
        self,
        order,
    ):
        return Decimal("0.00")

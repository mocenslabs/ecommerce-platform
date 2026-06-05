from apps.orders.services.tax.iva import (
    ArgentinaIVAStrategy,
)
from apps.orders.services.tax.no_tax import (
    NoTaxStrategy,
)


def calculate_tax_for_order(
    order,
):
    """
    Resolve tax strategy dynamically.
    """

    country = order.shipping_address.country

    if country == "AR":
        strategy = ArgentinaIVAStrategy()

    else:
        strategy = NoTaxStrategy()

    return strategy.calculate(
        order,
    )

from decimal import Decimal

from apps.orders.services.shipping.flat import (
    calculate_flat_shipping,
)
from apps.orders.services.shipping.free import (
    apply_free_shipping,
)


def calculate_shipping_for_order(
    order,
):
    """
    Central shipping calculation service.
    """

    shipping_method = order.shipping_method

    if not shipping_method:
        return Decimal("0.00")

    shipping_cost = calculate_flat_shipping(
        shipping_method.price,
    )

    shipping_cost = apply_free_shipping(
        subtotal=order.subtotal_amount,
        shipping_cost=shipping_cost,
        threshold=(shipping_method.free_shipping_threshold),
    )

    return shipping_cost

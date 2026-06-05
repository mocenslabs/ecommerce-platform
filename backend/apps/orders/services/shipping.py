from decimal import Decimal


def calculate_shipping_cost(
    subtotal,
    shipping_method,
):
    """
    Calculate shipping cost.
    """

    if not shipping_method:
        return Decimal("0.00")

    if (
        shipping_method.free_shipping_threshold
        and subtotal >= shipping_method.free_shipping_threshold
    ):
        return Decimal("0.00")

    return shipping_method.price

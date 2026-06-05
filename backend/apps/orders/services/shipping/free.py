from decimal import Decimal


def apply_free_shipping(
    subtotal,
    shipping_cost,
    threshold=None,
):
    """
    Apply free shipping rules.
    """

    if threshold and subtotal >= threshold:
        return Decimal("0.00")

    return shipping_cost

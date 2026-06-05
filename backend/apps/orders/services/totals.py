from decimal import Decimal

from apps.orders.services.shipping import (
    calculate_shipping_cost,
)


def calculate_order_totals(
    subtotal,
    shipping_method,
):
    """
    Calculate final order totals.
    """

    shipping_amount = calculate_shipping_cost(
        subtotal=subtotal,
        shipping_method=shipping_method,
    )

    tax_amount = Decimal("0.00")

    discount_amount = Decimal("0.00")

    total_amount = subtotal + shipping_amount + tax_amount - discount_amount

    return {
        "subtotal": subtotal,
        "shipping_amount": shipping_amount,
        "tax_amount": tax_amount,
        "discount_amount": discount_amount,
        "total_amount": total_amount,
    }

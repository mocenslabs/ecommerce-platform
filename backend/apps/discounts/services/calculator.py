from decimal import Decimal

from apps.discounts.constants import (
    DiscountType,
)


def calculate_discount_amount(
    discount,
    subtotal,
):
    """
    Calculate discount amount.
    """

    if discount.discount_type == DiscountType.PERCENTAGE:
        amount = (subtotal * discount.value) / Decimal("100")

    else:
        amount = discount.value

    if amount > subtotal:
        return subtotal

    return amount

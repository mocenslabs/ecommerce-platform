from django.utils import timezone

from apps.discounts.models import (
    Discount,
)


def validate_discount(
    discount: Discount,
    subtotal,
):
    """
    Validate discount usability.
    """

    if not discount.active:
        raise ValueError("Discount is inactive.")

    now = timezone.now()

    if discount.starts_at and discount.starts_at > now:
        raise ValueError("Discount not started yet.")

    if discount.expires_at and discount.expires_at < now:
        raise ValueError("Discount expired.")

    if discount.usage_limit is not None and discount.used_count >= discount.usage_limit:
        raise ValueError("Discount usage limit reached.")

    if subtotal < discount.minimum_amount:
        raise ValueError("Minimum amount not reached.")

    return True

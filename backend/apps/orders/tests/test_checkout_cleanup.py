import pytest

from apps.orders.services.checkout import (
    process_checkout,
)


@pytest.mark.django_db
def test_checkout_clears_cart(
    user,
    cart_with_items,
    shipping_address,
    shipping_method,
):
    """
    Ensure checkout clears cart items.
    """

    process_checkout(
        user=user,
        cart=cart_with_items,
        shipping_address=shipping_address,
        shipping_method=shipping_method,
    )

    assert cart_with_items.items.count() == 0

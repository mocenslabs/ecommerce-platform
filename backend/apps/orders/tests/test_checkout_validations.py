import pytest

from apps.orders.exceptions.checkout import (
    EmptyCartException,
)
from apps.orders.services.checkout import (
    process_checkout,
)


@pytest.mark.django_db
def test_checkout_with_empty_cart_raises_exception(
    user,
    cart,
    shipping_address,
    shipping_method,
):
    """
    Ensure checkout fails with empty cart.
    """

    with pytest.raises(
        EmptyCartException,
    ):
        process_checkout(
            user=user,
            cart=cart,
            shipping_address=shipping_address,
            shipping_method=shipping_method,
        )

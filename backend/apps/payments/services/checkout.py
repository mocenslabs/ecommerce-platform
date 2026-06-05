from apps.orders.services.order import (
    create_order_from_cart,
)
from apps.payments.services.payment import (
    create_payment_for_order,
)


def checkout_cart(
    *,
    cart,
    billing_address,
    shipping_address,
    email,
    provider_name,
    user=None,
):
    """
    Full checkout orchestration flow.

    Responsibilities:
    - create immutable order snapshot
    - initialize payment flow
    - prepare future stock reservation hooks

    Returns:
        tuple[Order, Payment]
    """
    order = create_order_from_cart(
        cart=cart,
        billing_address=billing_address,
        shipping_address=shipping_address,
        email=email,
        user=user,
    )

    payment = create_payment_for_order(
        order=order,
        provider_name=provider_name,
    )

    return order, payment

from decimal import Decimal

from apps.orders.models import (
    Order,
    OrderItem,
)


def create_order_from_cart(
    *,
    cart,
    billing_address,
    shipping_address,
    email: str,
    user=None,
) -> Order:
    """
    Create an immutable order snapshot from a cart instance.

    This process copies product pricing and product information
    into OrderItem records to preserve historical consistency,
    even if catalog data changes later.

    The cart itself remains mutable until explicitly checked out.

    Args:
        cart: Source cart instance.
        billing_address: Billing address instance.
        shipping_address: Shipping address instance.
        email: Customer email address.
        user: Optional authenticated user.

    Returns:
        Order: Newly created order instance.
    """
    subtotal = Decimal("0.00")

    order = Order.objects.create(
        user=user,
        email=email,
        billing_address=billing_address,
        shipping_address=shipping_address,
    )

    for item in cart.items.select_related(
        "variant",
        "variant__product",
    ):
        total_price = item.variant.price * item.quantity

        subtotal += total_price

        OrderItem.objects.create(
            order=order,
            product_name=item.variant.product.name,
            sku=item.variant.sku,
            quantity=item.quantity,
            unit_price=item.variant.price,
            total_price=total_price,
            variant=item.variant,
        )

    order.subtotal_amount = subtotal
    order.total_amount = subtotal

    order.save()

    return order

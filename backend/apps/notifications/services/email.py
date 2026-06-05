from django.conf import settings
from django.core.mail import (
    send_mail,
)

from apps.cart.models import (
    Cart,
)
from apps.orders.models import (
    Order,
)


def send_order_created_email(
    order_id,
):
    """
    Send order confirmation email.
    """

    order = Order.objects.get(
        id=order_id,
    )

    if not order.email:
        return

    send_mail(
        subject=(f"Order {order.order_number} created"),
        message=(f"Your order {order.order_number} was created successfully."),
        from_email=(settings.DEFAULT_FROM_EMAIL),
        recipient_list=[
            order.email,
        ],
        fail_silently=True,
    )


def send_order_paid_email(
    order_id,
):
    """
    Send payment confirmation email.
    """

    order = Order.objects.get(
        id=order_id,
    )

    if not order.email:
        return

    send_mail(
        subject=(f"Payment received for order {order.order_number}"),
        message=("Your payment was received successfully."),
        from_email=(settings.DEFAULT_FROM_EMAIL),
        recipient_list=[
            order.email,
        ],
        fail_silently=True,
    )


def send_abandoned_cart_email(
    cart_id,
):
    """
    Send abandoned cart reminder.
    """

    cart = Cart.objects.get(
        id=cart_id,
    )

    if not cart.user:
        return

    if not cart.user.email:
        return

    send_mail(
        subject="You left items in your cart",
        message=("Complete your purchase before products run out of stock."),
        from_email=(settings.DEFAULT_FROM_EMAIL),
        recipient_list=[
            cart.user.email,
        ],
        fail_silently=True,
    )

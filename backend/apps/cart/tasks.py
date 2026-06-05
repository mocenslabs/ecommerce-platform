from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from apps.cart.models import (
    Cart,
)
from apps.notifications.services.email import (
    send_abandoned_cart_email,
)


@shared_task
def send_abandoned_cart_reminders():
    """
    Send abandoned cart reminders.
    """

    cutoff = timezone.now() - timedelta(hours=1)

    carts = (
        Cart.objects.filter(
            updated_at__lte=cutoff,
        )
        .select_related(
            "user",
        )
        .prefetch_related(
            "items",
        )
    )

    for cart in carts:
        if not cart.user:
            continue

        if not cart.items.exists():
            continue

        send_abandoned_cart_email(
            cart.id,
        )

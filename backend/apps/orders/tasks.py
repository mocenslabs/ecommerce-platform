from celery import shared_task

from apps.core.tasks import (
    BaseTaskWithRetry,
)
from apps.orders.models import (
    Order,
)


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_order_confirmation_email(
    self,
    order_id,
):
    """
    Send confirmation email asynchronously.
    """

    order = Order.objects.get(
        id=order_id,
    )

    print(f"Sending confirmation email for order {order.id}")


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def handle_order_paid_event(
    self,
    payload,
):
    """
    Handle order paid domain event.
    """

    order_id = payload.get(
        "order_id",
    )

    print(f"Handling paid event for order {order_id}")

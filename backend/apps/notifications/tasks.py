from celery import shared_task

from apps.core.tasks import (
    BaseTaskWithRetry,
)
from apps.notifications.services.email import (
    send_order_created_email,
    send_order_paid_email,
)


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_order_created_email_task(
    self,
    order_id,
):
    """
    Send order created email asynchronously.
    """

    send_order_created_email(
        order_id,
    )


@shared_task(
    bind=True,
    base=BaseTaskWithRetry,
)
def send_order_paid_email_task(
    self,
    order_id,
):
    """
    Send order paid email asynchronously.
    """

    send_order_paid_email(
        order_id,
    )

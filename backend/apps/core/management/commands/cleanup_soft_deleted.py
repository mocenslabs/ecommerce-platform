from datetime import timedelta

from django.core.management.base import (
    BaseCommand,
)
from django.utils import timezone

from apps.orders.models import (
    Order,
)


class Command(
    BaseCommand,
):
    """
    Cleanup soft deleted records.
    """

    help = "Delete old soft deleted records."

    def handle(
        self,
        *args,
        **kwargs,
    ):
        threshold = timezone.now() - timedelta(days=90)

        deleted_orders = Order.all_objects.filter(
            is_deleted=True,
            deleted_at__lt=threshold,
        )

        count = deleted_orders.count()

        deleted_orders.delete()

        self.stdout.write(self.style.SUCCESS((f"Deleted {count} soft deleted orders.")))

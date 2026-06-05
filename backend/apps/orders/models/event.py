from django.db import models

from apps.core.models import BaseModel


class OrderEvent(BaseModel):
    """
    Store order timeline events.
    """

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="events",
    )

    event_type = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        blank=True,
    )

    metadata = models.JSONField(
        default=dict,
        blank=True,
    )

    def __str__(self):
        return f"{self.order.order_number} - {self.event_type}"

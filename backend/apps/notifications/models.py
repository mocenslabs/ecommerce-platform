from django.conf import settings
from django.db import models

from apps.core.models import BaseModel
from apps.notifications.constants import (
    NotificationType,
)


class Notification(BaseModel):
    """
    User notification record.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    notification_type = models.CharField(
        max_length=50,
        choices=NotificationType.CHOICES,
    )

    title = models.CharField(
        max_length=255,
    )

    message = models.TextField()

    read = models.BooleanField(
        default=False,
    )

    data = models.JSONField(
        default=dict,
        blank=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "user",
                    "read",
                ],
            ),
        ]

    def __str__(self):
        return f"{self.user.email} - {self.notification_type}"

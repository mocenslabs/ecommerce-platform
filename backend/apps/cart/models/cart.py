import uuid

from django.conf import settings
from django.db import models

from apps.core.models import BaseModel


class Cart(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="carts",
    )

    session_key = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    checked_out = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        if self.user:
            return f"Cart - {self.user.email}"

        return f"Anonymous Cart - {self.session_key}"

import uuid

from django.db import models
from django.utils import timezone

from apps.core.managers import (
    ActiveManager,
)


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    objects = ActiveManager()

    all_objects = models.Manager()

    class Meta:
        abstract = True

    def soft_delete(self):
        """
        Soft delete instance.
        """

        self.is_deleted = True

        self.deleted_at = timezone.now()

        self.save(
            update_fields=[
                "is_deleted",
                "deleted_at",
            ],
        )

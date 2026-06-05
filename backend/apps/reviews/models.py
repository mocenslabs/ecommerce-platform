from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint

from apps.core.models import BaseModel


class ProductReview(BaseModel):
    """
    Product review submitted by customer.
    """

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField()

    title = models.CharField(
        max_length=255,
    )

    comment = models.TextField(
        blank=True,
    )

    verified_purchase = models.BooleanField(
        default=False,
    )

    is_approved = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        constraints = [
            UniqueConstraint(
                fields=[
                    "product",
                    "user",
                ],
                name="unique_user_product_review",
            ),
        ]

        indexes = [
            models.Index(
                fields=[
                    "product",
                    "rating",
                ],
            ),
        ]

    def __str__(self):
        return f"{self.product.name} - {self.rating}"

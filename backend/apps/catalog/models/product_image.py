from django.db import models

from apps.core.models import BaseModel


class ProductImage(BaseModel):
    """
    Product gallery image.
    """

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="products/",
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    sort_order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = [
            "-is_primary",
            "sort_order",
            "created_at",
        ]

        indexes = [
            models.Index(
                fields=[
                    "product",
                    "is_primary",
                ],
            ),
        ]

    def __str__(self):
        return f"{self.product.name} image"

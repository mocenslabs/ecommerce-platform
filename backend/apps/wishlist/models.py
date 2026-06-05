from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint

from apps.core.models import BaseModel


class Wishlist(BaseModel):
    """
    Customer wishlist.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlist",
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"Wishlist - {self.user.email}"


class WishlistItem(BaseModel):
    """
    Wishlist saved product.
    """

    wishlist = models.ForeignKey(
        "wishlist.Wishlist",
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="wishlist_items",
    )

    class Meta:
        ordering = [
            "-created_at",
        ]

        constraints = [
            UniqueConstraint(
                fields=[
                    "wishlist",
                    "product",
                ],
                name="unique_wishlist_product",
            ),
        ]

    def __str__(self):
        return f"{self.wishlist.user.email} - {self.product.name}"

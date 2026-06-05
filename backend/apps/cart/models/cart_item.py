from django.db import models
from django.db.models import UniqueConstraint

from apps.core.models import BaseModel


class CartItem(BaseModel):
    cart = models.ForeignKey(
        "cart.Cart",
        on_delete=models.CASCADE,
        related_name="items",
    )

    variant = models.ForeignKey(
        "catalog.ProductVariant",
        on_delete=models.CASCADE,
        related_name="cart_items",
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["cart", "variant"],
                name="unique_cart_variant",
            )
        ]

    def __str__(self):
        return f"{self.variant.sku} x {self.quantity}"

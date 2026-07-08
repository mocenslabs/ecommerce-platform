from django.db import transaction

from apps.cart.models import (
    Cart,
    CartItem,
)
from apps.inventory.models import (
    Inventory,
)
from apps.orders.models import (
    Order,
)


@transaction.atomic
def reorder_order(
    *,
    user,
    order_number,
):
    """
    Recreate a previous order inside the user's cart.
    """

    order = Order.objects.prefetch_related(
        "items",
    ).get(
        order_number=order_number,
        user=user,
    )

    cart, _ = Cart.objects.get_or_create(
        user=user,
        checked_out=False,
    )

    added_items = []

    for item in order.items.select_related(
        "variant",
    ):
        variant = item.variant

        if not variant:
            continue

        inventory = Inventory.objects.select_for_update().get(
            variant=variant,
        )

        quantity_to_add = min(
            item.quantity,
            inventory.available_quantity,
        )

        if quantity_to_add <= 0:
            continue

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            variant=variant,
            defaults={
                "quantity": quantity_to_add,
            },
        )

        if not created:
            cart_item.quantity += quantity_to_add

            cart_item.save(
                update_fields=[
                    "quantity",
                ],
            )

        added_items.append(
            variant.sku,
        )

    return {
        "cart": cart,
        "items_added": added_items,
    }

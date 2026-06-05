from apps.cart.models import Cart


def get_cart_with_items(cart_id):
    return (
        Cart.objects.select_related(
            "user",
        )
        .prefetch_related(
            "items",
            "items__variant",
            "items__variant__product",
        )
        .get(id=cart_id)
    )

from apps.cart.models import CartItem


def add_item_to_cart(
    *,
    cart,
    variant,
    quantity=1,
):
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        variant=variant,
        defaults={
            "quantity": quantity,
        },
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    return cart_item

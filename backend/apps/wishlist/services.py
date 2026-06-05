from apps.catalog.models import Product
from apps.wishlist.models import (
    Wishlist,
    WishlistItem,
)


def get_or_create_wishlist(
    user,
):
    """
    Return user wishlist.
    """

    wishlist, _ = Wishlist.objects.get_or_create(
        user=user,
    )

    return wishlist


def add_product_to_wishlist(
    user,
    product: Product,
):
    """
    Add product to wishlist.
    """

    wishlist = get_or_create_wishlist(
        user,
    )

    item, _ = WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product,
    )

    return item


def remove_product_from_wishlist(
    user,
    product: Product,
):
    """
    Remove product from wishlist.
    """

    wishlist = get_or_create_wishlist(
        user,
    )

    WishlistItem.objects.filter(
        wishlist=wishlist,
        product=product,
    ).delete()

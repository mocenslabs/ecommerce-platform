from django.db.models import Sum

from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.models import (
    Address,
    Order,
)
from apps.wishlist.models import (
    WishlistItem,
)


def get_customer_dashboard(user):
    """
    Return customer dashboard data.
    """

    orders = Order.objects.filter(
        user=user,
    )

    total_orders = orders.count()

    total_spent = (
        orders.filter(
            status=OrderStatus.PAID,
        ).aggregate(
            total=Sum(
                "total_amount",
            ),
        )["total"]
        or 0
    )

    wishlist_count = WishlistItem.objects.filter(
        wishlist__user=user,
    ).count()

    address_count = Address.objects.filter(
        user=user,
    ).count()

    last_order = orders.order_by(
        "-created_at",
    ).first()

    return {
        "total_orders": total_orders,
        "total_spent": total_spent,
        "wishlist_count": wishlist_count,
        "address_count": address_count,
        "last_order": last_order,
    }

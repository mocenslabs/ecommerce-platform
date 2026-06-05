from decimal import Decimal

from django.contrib.auth import (
    get_user_model,
)
from django.db.models import Count, Sum

from apps.catalog.models import Product
from apps.orders.constants import (
    OrderStatus,
)
from apps.orders.models import (
    Order,
)

User = get_user_model()


def get_dashboard_stats():
    """
    Return dashboard KPIs.
    """

    total_revenue = Order.objects.filter(
        status=OrderStatus.PAID,
    ).aggregate(
        total=Sum(
            "total_amount",
        )
    )["total"] or Decimal("0.00")

    total_orders = Order.objects.count()

    paid_orders = Order.objects.filter(
        status=OrderStatus.PAID,
    ).count()

    pending_orders = Order.objects.filter(
        status=OrderStatus.PENDING,
    ).count()

    cancelled_orders = Order.objects.filter(
        status=OrderStatus.CANCELLED,
    ).count()

    total_customers = User.objects.count()

    total_products = Product.objects.count()

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "paid_orders": paid_orders,
        "pending_orders": pending_orders,
        "cancelled_orders": cancelled_orders,
        "total_customers": (total_customers),
        "total_products": (total_products),
    }


def get_top_products(
    limit=5,
):
    """
    Return best selling products.
    """

    return Product.objects.annotate(
        total_sales=Count(
            "variants__orderitem",
        ),
    ).order_by(
        "-total_sales",
    )[:limit]


def get_recent_orders(
    limit=10,
):
    """
    Return recent orders.
    """

    return Order.objects.select_related(
        "user",
    ).order_by(
        "-created_at",
    )[:limit]

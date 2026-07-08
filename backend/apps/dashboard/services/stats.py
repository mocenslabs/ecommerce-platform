from decimal import Decimal

from django.contrib.auth import (
    get_user_model,
)
from django.db.models import (
    Count,
    F,
    Sum,
)
from django.db.models.functions import (
    TruncMonth,
)

from apps.catalog.models import (
    Product,
)
from apps.inventory.constants import (
    InventoryReservationStatus,
)
from apps.inventory.models import (
    Inventory,
    InventoryReservation,
)
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
        "total_customers": total_customers,
        "total_products": total_products,
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


def get_revenue_trend():
    """
    Revenue grouped by month.
    """

    return (
        Order.objects.filter(
            status=OrderStatus.PAID,
        )
        .annotate(
            month=TruncMonth(
                "created_at",
            ),
        )
        .values(
            "month",
        )
        .annotate(
            revenue=Sum(
                "total_amount",
            ),
        )
        .order_by(
            "month",
        )
    )


def get_orders_by_status():
    """
    Orders grouped by status.
    """

    return (
        Order.objects.values(
            "status",
        )
        .annotate(
            total=Count(
                "id",
            ),
        )
        .order_by()
    )


def get_low_stock_products():
    """
    Products with low stock.
    """

    return (
        Inventory.objects.select_related(
            "variant",
            "variant__product",
        )
        .filter(
            quantity__lte=5,
        )
        .order_by(
            "quantity",
        )[:10]
    )


def get_inventory_health():
    """
    Return inventory health KPIs.
    """

    total_stock = (
        Inventory.objects.aggregate(
            total=Sum("quantity"),
        )["total"]
        or 0
    )

    reserved_stock = (
        Inventory.objects.aggregate(
            total=Sum("reserved_quantity"),
        )["total"]
        or 0
    )

    available_stock = total_stock - reserved_stock

    reserved_percentage = (
        round(
            (reserved_stock / total_stock) * 100,
            2,
        )
        if total_stock > 0
        else 0
    )

    return {
        "total_stock": total_stock,
        "reserved_stock": reserved_stock,
        "available_stock": available_stock,
        "reserved_percentage": reserved_percentage,
    }


def get_reserved_inventory():
    """
    Return inventory currently reserved.
    """

    return (
        Inventory.objects.select_related(
            "variant",
            "variant__product",
        )
        .filter(
            reserved_quantity__gt=0,
        )
        .order_by(
            "-reserved_quantity",
        )
    )


def get_expired_reservations(
    limit=20,
):
    """
    Return recently expired reservations.
    """

    return (
        InventoryReservation.objects.select_related(
            "variant",
        )
        .filter(
            status=(InventoryReservationStatus.EXPIRED),
        )
        .order_by(
            "-updated_at",
        )[:limit]
    )

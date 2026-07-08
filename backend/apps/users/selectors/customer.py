from django.contrib.auth import get_user_model
from django.db.models import Count, Sum

from apps.users.models.roles import (
    UserRole,
)

User = get_user_model()


def get_customers():
    """
    Return customers with stats.
    """

    return (
        User.objects.filter(
            role=UserRole.CUSTOMER,
        )
        .annotate(
            orders_count=Count(
                "orders",
                distinct=True,
            ),
            total_spent=Sum(
                "orders__total_amount",
            ),
        )
        .order_by(
            "-date_joined",
        )
    )

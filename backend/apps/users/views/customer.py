from rest_framework.generics import (
    ListAPIView,
)

from apps.core.permissions.roles import (
    IsAdminUserRole,
)
from apps.users.selectors.customer import (
    get_customers,
)
from apps.users.serializers.customer import (
    CustomerSerializer,
)


class AdminCustomerListAPIView(
    ListAPIView,
):
    """
    Admin customers list.
    """

    serializer_class = CustomerSerializer

    permission_classes = [
        IsAdminUserRole,
    ]

    def get_queryset(
        self,
    ):
        return get_customers()

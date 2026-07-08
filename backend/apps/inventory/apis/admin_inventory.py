from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.inventory.models import (
    Inventory,
)
from apps.inventory.serializers.admin_inventory import (
    AdminInventorySerializer,
)


class AdminInventoryListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Inventory.objects.select_related(
        "variant",
    )

    serializer_class = AdminInventorySerializer


class AdminInventoryDetailApi(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Inventory.objects.select_related(
        "variant",
    )

    serializer_class = AdminInventorySerializer

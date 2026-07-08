from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.catalog.models import (
    ProductVariant,
)
from apps.catalog.serializers.admin_variant import (
    AdminVariantSerializer,
)


class AdminVariantListCreateApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ProductVariant.objects.select_related(
        "product",
    )

    serializer_class = AdminVariantSerializer


class AdminVariantDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ProductVariant.objects.select_related(
        "product",
    )

    serializer_class = AdminVariantSerializer

from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.catalog.models import (
    Product,
)
from apps.catalog.serializers.admin_product import (
    AdminProductCreateUpdateSerializer,
    AdminProductSerializer,
)


class AdminProductListCreateApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Product.objects.select_related(
        "category",
        "brand",
    )

    def get_serializer_class(
        self,
    ):
        if self.request.method == "POST":
            return AdminProductCreateUpdateSerializer

        return AdminProductSerializer


class AdminProductDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Product.objects.select_related(
        "category",
        "brand",
    )

    def get_serializer_class(
        self,
    ):
        if self.request.method in [
            "PUT",
            "PATCH",
        ]:
            return AdminProductCreateUpdateSerializer

        return AdminProductSerializer

from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.catalog.models import (
    ProductImage,
)
from apps.catalog.serializers.admin_product_image import (
    AdminProductImageCreateUpdateSerializer,
    AdminProductImageSerializer,
)


class AdminProductImageListCreateApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ProductImage.objects.select_related(
        "product",
    )

    def get_serializer_class(
        self,
    ):
        if self.request.method == "POST":
            return AdminProductImageCreateUpdateSerializer

        return AdminProductImageSerializer


class AdminProductImageDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ProductImage.objects.select_related(
        "product",
    )

    def get_serializer_class(
        self,
    ):
        if self.request.method in [
            "PUT",
            "PATCH",
        ]:
            return AdminProductImageCreateUpdateSerializer

        return AdminProductImageSerializer

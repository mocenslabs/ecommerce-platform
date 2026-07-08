from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.catalog.models import (
    Brand,
)
from apps.catalog.serializers.admin_brand import (
    AdminBrandSerializer,
)


class AdminBrandListCreateApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Brand.objects.all()

    serializer_class = AdminBrandSerializer


class AdminBrandDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Brand.objects.all()

    serializer_class = AdminBrandSerializer

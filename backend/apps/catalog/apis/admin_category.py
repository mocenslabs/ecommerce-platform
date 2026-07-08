from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.catalog.models import (
    Category,
)
from apps.catalog.serializers.admin_category import (
    AdminCategorySerializer,
)


class AdminCategoryListCreateApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Category.objects.select_related(
        "parent",
    )

    serializer_class = AdminCategorySerializer


class AdminCategoryDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Category.objects.select_related(
        "parent",
    )

    serializer_class = AdminCategorySerializer

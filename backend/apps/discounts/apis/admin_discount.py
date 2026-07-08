from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.discounts.models import (
    Discount,
)
from apps.discounts.serializers.admin_discount import (
    AdminDiscountSerializer,
)


class AdminDiscountListApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Discount.objects.all().order_by("-created_at")

    serializer_class = AdminDiscountSerializer


class AdminDiscountDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = Discount.objects.all()

    serializer_class = AdminDiscountSerializer

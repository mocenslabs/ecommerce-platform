from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.orders.models import (
    ShippingMethod,
)
from apps.orders.serializers.admin_shipping_method import (
    AdminShippingMethodSerializer,
)


class AdminShippingMethodListApi(
    generics.ListCreateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ShippingMethod.objects.all().order_by("name")

    serializer_class = AdminShippingMethodSerializer


class AdminShippingMethodDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ShippingMethod.objects.all()

    serializer_class = AdminShippingMethodSerializer

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.orders.models import (
    ShippingMethod,
)
from apps.orders.serializers.shipping_method import (
    ShippingMethodSerializer,
)


class ShippingMethodListApi(
    generics.ListAPIView,
):
    """
    Return active shipping methods.
    """

    serializer_class = ShippingMethodSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    queryset = ShippingMethod.objects.filter(
        active=True,
    )

from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.orders.models import Address
from apps.orders.serializers.address import (
    AddressSerializer,
)


class AddressListCreateApi(
    generics.ListCreateAPIView,
):
    """
    List and create user addresses.
    """

    serializer_class = AddressSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """
        Return authenticated
        user addresses.
        """

        return Address.objects.filter(
            user=self.request.user,
        )

    def perform_create(
        self,
        serializer,
    ):
        """
        Attach address to user.
        """

        serializer.save(
            user=self.request.user,
        )


class AddressDetailApi(
    generics.RetrieveUpdateDestroyAPIView,
):
    """
    Manage single address.
    """

    serializer_class = AddressSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """
        Return authenticated
        user addresses.
        """

        return Address.objects.filter(
            user=self.request.user,
        )

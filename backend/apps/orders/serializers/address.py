from rest_framework import serializers

from apps.orders.models import Address


class AddressSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize customer addresses.
    """

    class Meta:
        model = Address

        exclude = [
            "user",
        ]

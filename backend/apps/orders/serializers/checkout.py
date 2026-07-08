from rest_framework import serializers

from apps.orders.models import (
    Address,
    ShippingMethod,
)


class CheckoutSerializer(
    serializers.Serializer,
):
    shipping_address_id = serializers.UUIDField()

    billing_address_id = serializers.UUIDField(
        required=False,
    )

    shipping_method_id = serializers.UUIDField()

    discount_code = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    def validate_shipping_address_id(
        self,
        value,
    ):
        if not Address.objects.filter(
            id=value,
        ).exists():
            raise serializers.ValidationError("Invalid shipping address.")

        return value

    def validate_billing_address_id(
        self,
        value,
    ):
        if not Address.objects.filter(
            id=value,
        ).exists():
            raise serializers.ValidationError("Invalid billing address.")

        return value

    def validate_shipping_method_id(
        self,
        value,
    ):
        if not ShippingMethod.objects.filter(
            id=value,
            active=True,
        ).exists():
            raise serializers.ValidationError("Invalid shipping method.")

        return value

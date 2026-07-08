from rest_framework import serializers

from apps.discounts.models import Discount


class AdminDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount

        fields = (
            "id",
            "code",
            "discount_type",
            "value",
            "minimum_amount",
            "usage_limit",
            "used_count",
            "active",
            "starts_at",
            "expires_at",
            "created_at",
        )

from rest_framework import serializers

from apps.users.models.user import User


class CustomerSerializer(
    serializers.ModelSerializer,
):
    orders_count = serializers.IntegerField(
        read_only=True,
    )

    total_spent = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = User

        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "is_verified",
            "date_joined",
            "orders_count",
            "total_spent",
        )

from rest_framework import serializers

from apps.catalog.models import (
    Category,
)


class AdminCategorySerializer(
    serializers.ModelSerializer,
):
    parent_name = serializers.CharField(
        source="parent.name",
        read_only=True,
    )

    class Meta:
        model = Category

        fields = [
            "id",
            "name",
            "slug",
            "description",
            "parent",
            "parent_name",
            "created_at",
            "is_active",
        ]

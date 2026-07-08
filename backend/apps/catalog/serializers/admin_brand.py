from rest_framework import serializers

from apps.catalog.models import (
    Brand,
)


class AdminBrandSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = Brand

        fields = [
            "id",
            "name",
            "slug",
            "description",
            "created_at",
            "is_active",
        ]

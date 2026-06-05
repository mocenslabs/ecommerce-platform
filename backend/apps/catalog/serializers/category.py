from rest_framework import serializers

from apps.catalog.models import (
    Category,
)


class CategorySerializer(
    serializers.ModelSerializer,
):
    """
    Serialize catalog categories.
    """

    class Meta:
        model = Category

        fields = [
            "id",
            "name",
            "slug",
            "description",
            "parent",
        ]

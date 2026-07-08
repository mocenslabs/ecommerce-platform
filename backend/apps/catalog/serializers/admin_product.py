from rest_framework import serializers

from apps.catalog.models import (
    Product,
)


class AdminProductSerializer(
    serializers.ModelSerializer,
):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    brand_name = serializers.CharField(
        source="brand.name",
        read_only=True,
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "description",
            "category",
            "category_name",
            "brand",
            "brand_name",
            "is_featured",
            "is_active",
            "average_rating",
            "reviews_count",
            "created_at",
        ]


class AdminProductCreateUpdateSerializer(
    serializers.ModelSerializer,
):
    class Meta:
        model = Product

        fields = [
            "name",
            "short_description",
            "description",
            "category",
            "brand",
            "is_featured",
            "is_active",
        ]

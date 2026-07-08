from rest_framework import serializers

from apps.catalog.models import (
    Product,
)
from apps.catalog.serializers.brand import (
    BrandSerializer,
)
from apps.catalog.serializers.category import (
    CategorySerializer,
)
from apps.catalog.serializers.product_image import (
    ProductImageSerializer,
)
from apps.catalog.serializers.product_variant import (
    ProductVariantSerializer,
)


class ProductListSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize product list items.
    """

    primary_image = serializers.SerializerMethodField()

    price = serializers.SerializerMethodField()

    category = CategorySerializer(
        read_only=True,
    )

    brand = BrandSerializer(
        read_only=True,
    )

    def get_primary_image(
        self,
        obj,
    ):
        """
        Return primary product image.
        """

        image = obj.images.filter(
            is_primary=True,
        ).first()

        if not image:
            return None

        return ProductImageSerializer(
            image,
        ).data

    def get_price(
        self,
        obj,
    ):
        """
        Return first variant price.
        """

        variant = obj.variants.first()

        if not variant:
            return None

        return variant.price

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "is_featured",
            "category",
            "brand",
            "price",
            "primary_image",
            "average_rating",
            "reviews_count",
        ]


class ProductDetailSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize product details.
    """

    category = CategorySerializer(
        read_only=True,
    )

    brand = BrandSerializer(
        read_only=True,
    )

    variants = ProductVariantSerializer(
        many=True,
        read_only=True,
    )

    images = ProductImageSerializer(
        many=True,
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
            "is_featured",
            "category",
            "brand",
            "variants",
            "images",
            "average_rating",
            "reviews_count",
        ]

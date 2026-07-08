from rest_framework import serializers

from apps.reviews.models import (
    ProductReview,
)


class AdminReviewSerializer(
    serializers.ModelSerializer,
):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    customer_email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    class Meta:
        model = ProductReview

        fields = [
            "id",
            "product",
            "product_name",
            "user",
            "customer_email",
            "rating",
            "title",
            "comment",
            "verified_purchase",
            "is_approved",
            "created_at",
        ]

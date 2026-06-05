from rest_framework import serializers

from apps.reviews.models import (
    ProductReview,
)


class ProductReviewSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize product reviews.
    """

    user_name = serializers.CharField(
        source="user.first_name",
        read_only=True,
    )

    class Meta:
        model = ProductReview

        fields = [
            "id",
            "user_name",
            "rating",
            "title",
            "comment",
            "verified_purchase",
            "created_at",
        ]


class CreateProductReviewSerializer(
    serializers.ModelSerializer,
):
    """
    Create product review serializer.
    """

    class Meta:
        model = ProductReview

        fields = [
            "rating",
            "title",
            "comment",
        ]

    def validate_rating(
        self,
        value,
    ):
        """
        Validate rating range.
        """

        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")

        return value

    def validate(
        self,
        attrs,
    ):
        """
        Prevent duplicate reviews.
        """

        request = self.context.get(
            "request",
        )

        if not request:
            return attrs

        product_slug = self.context.get(
            "product_slug",
        )

        if not product_slug:
            return attrs

        exists = ProductReview.objects.filter(
            user=request.user,
            product__slug=product_slug,
        ).exists()

        if exists:
            raise serializers.ValidationError(
                ("You have already reviewed this product.")
            )

        return attrs


class UpdateProductReviewSerializer(
    serializers.ModelSerializer,
):
    """
    Update product review serializer.
    """

    class Meta:
        model = ProductReview

        fields = [
            "rating",
            "title",
            "comment",
        ]

    def validate_rating(
        self,
        value,
    ):
        """
        Validate rating range.
        """

        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")

        return value

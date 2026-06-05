from django.shortcuts import (
    get_object_or_404,
)
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)

from apps.catalog.models import (
    Product,
)
from apps.reviews.models import (
    ProductReview,
)
from apps.reviews.serializers import (
    CreateProductReviewSerializer,
    ProductReviewSerializer,
    UpdateProductReviewSerializer,
)
from apps.reviews.services import (
    update_product_rating,
)


class ProductReviewListApi(
    generics.ListAPIView,
):
    """
    List approved product reviews.
    """

    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        """
        Return approved product reviews.
        """

        product_slug = self.kwargs["slug"]

        return ProductReview.objects.select_related("user").filter(
            product__slug=product_slug,
            is_approved=True,
        )


class ProductReviewCreateApi(
    generics.CreateAPIView,
):
    """
    Create product review.
    """

    serializer_class = CreateProductReviewSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get_serializer_context(
        self,
    ):
        """
        Add product information.
        """

        context = super().get_serializer_context()

        context["product_slug"] = self.kwargs["slug"]

        return context

    def perform_create(
        self,
        serializer,
    ):
        """
        Save review.
        """

        product = get_object_or_404(
            Product,
            slug=self.kwargs["slug"],
        )

        review = serializer.save(
            user=self.request.user,
            product=product,
        )

        update_product_rating(
            product,
        )

        return review


class ProductReviewUpdateApi(
    generics.UpdateAPIView,
):
    """
    Update user review.
    """

    serializer_class = UpdateProductReviewSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get_queryset(
        self,
    ):
        """
        Only allow owner reviews.
        """

        return ProductReview.objects.filter(
            user=self.request.user,
        )

    def perform_update(
        self,
        serializer,
    ):
        """
        Update review and product rating.
        """

        review = serializer.save()

        update_product_rating(
            review.product,
        )


class ProductReviewDeleteApi(
    generics.DestroyAPIView,
):
    """
    Delete user review.
    """

    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get_queryset(
        self,
    ):
        """
        Only allow owner reviews.
        """

        return ProductReview.objects.filter(
            user=self.request.user,
        )

    def perform_destroy(
        self,
        instance,
    ):
        """
        Delete review and recalculate rating.
        """

        product = instance.product

        instance.delete()

        update_product_rating(
            product,
        )

from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
)

from apps.reviews.models import (
    ProductReview,
)
from apps.reviews.serializers.admin_review import (
    AdminReviewSerializer,
)


class AdminReviewListApi(
    generics.ListAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = (
        ProductReview.objects.select_related(
            "product",
            "user",
        )
        .all()
        .order_by(
            "-created_at",
        )
    )

    serializer_class = AdminReviewSerializer


class AdminReviewDetailApi(
    generics.RetrieveUpdateAPIView,
):
    permission_classes = [
        IsAdminUser,
    ]

    queryset = ProductReview.objects.select_related(
        "product",
        "user",
    ).all()

    serializer_class = AdminReviewSerializer

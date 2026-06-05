from django_filters.rest_framework import (
    DjangoFilterBackend,
)
from rest_framework import filters, generics

from apps.catalog.filters.product import (
    ProductFilter,
)
from apps.catalog.models import (
    Product,
)
from apps.catalog.serializers.product import (
    ProductDetailSerializer,
    ProductListSerializer,
)


class ProductListApi(
    generics.ListAPIView,
):
    """
    List catalog products.
    """

    serializer_class = ProductListSerializer

    queryset = (
        Product.objects.select_related(
            "category",
            "brand",
        )
        .prefetch_related(
            "images",
        )
        .all()
    )

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "brand",
        "is_featured",
        "is_active",
    ]

    search_fields = [
        "name",
        "slug",
        "short_description",
        "description",
    ]

    ordering_fields = [
        "created_at",
        "name",
    ]

    ordering = [
        "-created_at",
    ]

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_class = ProductFilter


class FeaturedProductListApi(
    generics.ListAPIView,
):
    """
    List featured products.
    """

    serializer_class = ProductListSerializer

    queryset = (
        Product.objects.select_related(
            "category",
            "brand",
        )
        .prefetch_related(
            "images",
        )
        .filter(
            is_featured=True,
            is_active=True,
        )
    )


class ProductDetailApi(
    generics.RetrieveAPIView,
):
    """
    Retrieve product details.
    """

    serializer_class = ProductDetailSerializer

    lookup_field = "slug"

    queryset = Product.objects.select_related(
        "category",
        "brand",
    ).prefetch_related(
        "variants",
        "images",
    )

import django_filters

from apps.catalog.models import (
    Product,
)


class ProductFilter(
    django_filters.FilterSet,
):
    """
    Product filtering.
    """

    min_price = django_filters.NumberFilter(
        field_name=("variants__price"),
        lookup_expr="gte",
    )

    max_price = django_filters.NumberFilter(
        field_name=("variants__price"),
        lookup_expr="lte",
    )

    category = django_filters.CharFilter(
        field_name=("category__slug"),
    )

    brand = django_filters.CharFilter(
        field_name=("brand__slug"),
    )

    featured = django_filters.BooleanFilter(
        field_name="is_featured",
    )

    search = django_filters.CharFilter(
        method="filter_search",
    )

    ordering = django_filters.OrderingFilter(
        fields=(
            (
                "created_at",
                "created_at",
            ),
            (
                "name",
                "name",
            ),
            (
                "average_rating",
                "rating",
            ),
        ),
    )

    class Meta:
        model = Product

        fields = []

    def filter_search(
        self,
        queryset,
        name,
        value,
    ):
        """
        Product text search.
        """

        return queryset.filter(
            name__icontains=value,
        )

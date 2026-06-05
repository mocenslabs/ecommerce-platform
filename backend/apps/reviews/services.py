from django.db.models import Avg, Count

from apps.catalog.models import Product
from apps.reviews.models import (
    ProductReview,
)


def update_product_rating(
    product: Product,
):
    """
    Update aggregated product rating data.
    """

    aggregation = ProductReview.objects.filter(
        product=product,
        is_approved=True,
    ).aggregate(
        average=Avg("rating"),
        count=Count("id"),
    )

    average_rating = aggregation["average"] or 0

    reviews_count = aggregation["count"] or 0

    product.average_rating = round(
        average_rating,
        2,
    )

    product.reviews_count = reviews_count

    product.save(
        update_fields=[
            "average_rating",
            "reviews_count",
        ],
    )

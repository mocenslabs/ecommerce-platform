from django.urls import path

from apps.reviews.apis import (
    ProductReviewCreateApi,
    ProductReviewDeleteApi,
    ProductReviewListApi,
    ProductReviewUpdateApi,
)

urlpatterns = [
    path(
        "products/<slug:slug>/reviews/",
        ProductReviewListApi.as_view(),
        name="product-reviews",
    ),
    path(
        "products/<slug:slug>/reviews/create/",
        ProductReviewCreateApi.as_view(),
        name="create-product-review",
    ),
    path(
        "reviews/<uuid:pk>/update/",
        ProductReviewUpdateApi.as_view(),
        name="update-product-review",
    ),
    path(
        "reviews/<uuid:pk>/delete/",
        ProductReviewDeleteApi.as_view(),
        name="delete-product-review",
    ),
]

from django.urls import path

from apps.catalog.apis.product import (
    FeaturedProductListApi,
    ProductDetailApi,
    ProductListApi,
)

urlpatterns = [
    path(
        "products/",
        ProductListApi.as_view(),
        name="product-list",
    ),
    path(
        "products/featured/",
        FeaturedProductListApi.as_view(),
        name="featured-products",
    ),
    path(
        "products/<slug:slug>/",
        ProductDetailApi.as_view(),
        name="product-detail",
    ),
]

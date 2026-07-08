from django.urls import path

from apps.catalog.apis.admin_brand import (
    AdminBrandDetailApi,
    AdminBrandListCreateApi,
)
from apps.catalog.apis.admin_category import (
    AdminCategoryDetailApi,
    AdminCategoryListCreateApi,
)
from apps.catalog.apis.admin_product import (
    AdminProductDetailApi,
    AdminProductListCreateApi,
)
from apps.catalog.apis.admin_product_image import (
    AdminProductImageDetailApi,
    AdminProductImageListCreateApi,
)
from apps.catalog.apis.admin_variant import (
    AdminVariantDetailApi,
    AdminVariantListCreateApi,
)
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
    path(
        "admin/products/",
        AdminProductListCreateApi.as_view(),
        name="admin-product-list",
    ),
    path(
        "admin/products/<uuid:pk>/",
        AdminProductDetailApi.as_view(),
        name="admin-product-detail",
    ),
    path(
        "admin/categories/",
        AdminCategoryListCreateApi.as_view(),
        name="admin-category-list",
    ),
    path(
        "admin/categories/<uuid:pk>/",
        AdminCategoryDetailApi.as_view(),
        name="admin-category-detail",
    ),
    path(
        "admin/brands/",
        AdminBrandListCreateApi.as_view(),
        name="admin-brand-list",
    ),
    path(
        "admin/brands/<uuid:pk>/",
        AdminBrandDetailApi.as_view(),
        name="admin-brand-detail",
    ),
    path(
        "admin/variants/",
        AdminVariantListCreateApi.as_view(),
        name="admin-variant-list",
    ),
    path(
        "admin/variants/<uuid:pk>/",
        AdminVariantDetailApi.as_view(),
        name="admin-variant-detail",
    ),
    path(
        "admin/product-images/",
        AdminProductImageListCreateApi.as_view(),
        name="admin-product-image-list",
    ),
    path(
        "admin/product-images/<uuid:pk>/",
        AdminProductImageDetailApi.as_view(),
        name="admin-product-image-detail",
    ),
]

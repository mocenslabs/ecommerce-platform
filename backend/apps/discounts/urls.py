from django.urls import path

from apps.discounts.apis.admin_discount import (
    AdminDiscountDetailApi,
    AdminDiscountListApi,
)

urlpatterns = [
    path(
        "admin/",
        AdminDiscountListApi.as_view(),
        name="admin-discounts",
    ),
    path(
        "admin/<uuid:pk>/",
        AdminDiscountDetailApi.as_view(),
        name="admin-discount-detail",
    ),
]

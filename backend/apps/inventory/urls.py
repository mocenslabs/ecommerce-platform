from django.urls import path

from apps.inventory.apis.admin_inventory import (
    AdminInventoryDetailApi,
    AdminInventoryListApi,
)

urlpatterns = [
    path(
        "admin/",
        AdminInventoryListApi.as_view(),
        name="admin-inventory-list",
    ),
    path(
        "admin/<uuid:pk>/",
        AdminInventoryDetailApi.as_view(),
        name="admin-inventory-detail",
    ),
]

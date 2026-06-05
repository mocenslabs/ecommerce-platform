from django.urls import path

from apps.dashboard.apis import (
    DashboardRecentOrdersApi,
    DashboardStatsApi,
    DashboardTopProductsApi,
)

urlpatterns = [
    path(
        "stats/",
        DashboardStatsApi.as_view(),
        name="dashboard-stats",
    ),
    path(
        "top-products/",
        DashboardTopProductsApi.as_view(),
        name="dashboard-top-products",
    ),
    path(
        "recent-orders/",
        DashboardRecentOrdersApi.as_view(),
        name="dashboard-recent-orders",
    ),
]

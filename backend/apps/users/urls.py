from django.urls import path

from apps.users.apis.change_password import (
    ChangePasswordApi,
)
from apps.users.apis.dashboard import (
    CustomerDashboardApi,
)
from apps.users.apis.profile import (
    ProfileApi,
)
from apps.users.views.customer import (
    AdminCustomerListAPIView,
)

urlpatterns = [
    path(
        "admin/customers/",
        AdminCustomerListAPIView.as_view(),
        name="admin-customers",
    ),
    path(
        "dashboard/",
        CustomerDashboardApi.as_view(),
        name="customer-dashboard",
    ),
    path(
        "profile/",
        ProfileApi.as_view(),
        name="profile",
    ),
    path(
        "change-password/",
        ChangePasswordApi.as_view(),
        name="change-password",
    ),
]

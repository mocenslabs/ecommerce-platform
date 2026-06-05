from django.urls import path

from apps.orders.apis.address import (
    AddressDetailApi,
    AddressListCreateApi,
)
from apps.orders.apis.checkout import (
    CheckoutApi,
)
from apps.orders.apis.order import (
    OrderDetailApi,
    OrderListApi,
)

urlpatterns = [
    path(
        "checkout/",
        CheckoutApi.as_view(),
        name="checkout",
    ),
    path(
        "",
        OrderListApi.as_view(),
        name="orders-list",
    ),
    path(
        "<uuid:order_number>/",
        OrderDetailApi.as_view(),
        name="order-detail",
    ),
    path(
        "addresses/",
        AddressListCreateApi.as_view(),
        name="address-list",
    ),
    path(
        "addresses/<int:pk>/",
        AddressDetailApi.as_view(),
        name="address-detail",
    ),
]

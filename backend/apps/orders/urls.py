from django.urls import path

from apps.orders.apis.address import (
    AddressDetailApi,
    AddressListCreateApi,
)
from apps.orders.apis.admin_order import (
    AdminOrderDetailApi,
    AdminOrderListApi,
)
from apps.orders.apis.admin_order_status import (
    AdminOrderStatusApi,
)
from apps.orders.apis.admin_shipping_method import (
    AdminShippingMethodDetailApi,
    AdminShippingMethodListApi,
)
from apps.orders.apis.admin_status import (
    AdminOrderDeliveredApi,
    AdminOrderProcessingApi,
    AdminOrderRefundApi,
    AdminOrderShippedApi,
)
from apps.orders.apis.cancel_order import CancelOrderApi
from apps.orders.apis.checkout import (
    CheckoutApi,
)
from apps.orders.apis.order import (
    OrderDetailApi,
    OrderListApi,
)
from apps.orders.apis.reorder import (
    ReorderApi,
)
from apps.orders.apis.shipping_method import ShippingMethodListApi

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
    path(
        "shipping-methods/",
        ShippingMethodListApi.as_view(),
        name="shipping-methods",
    ),
    path(
        "admin/",
        AdminOrderListApi.as_view(),
        name="admin-order-list",
    ),
    path(
        "admin/<uuid:pk>/",
        AdminOrderDetailApi.as_view(),
        name="admin-order-detail",
    ),
    path(
        "admin/<uuid:order_number>/processing/",
        AdminOrderProcessingApi.as_view(),
        name="admin-order-processing",
    ),
    path(
        "admin/<uuid:order_number>/shipped/",
        AdminOrderShippedApi.as_view(),
        name="admin-order-shipped",
    ),
    path(
        "admin/<uuid:order_number>/delivered/",
        AdminOrderDeliveredApi.as_view(),
        name="admin-order-delivered",
    ),
    path(
        "admin/<uuid:order_number>/refund/",
        AdminOrderRefundApi.as_view(),
        name="admin-order-refund",
    ),
    path(
        "admin/shipping-methods/",
        AdminShippingMethodListApi.as_view(),
        name="admin-shipping-methods",
    ),
    path(
        "admin/shipping-methods/<int:pk>/",
        AdminShippingMethodDetailApi.as_view(),
        name="admin-shipping-method-detail",
    ),
    path(
        "<uuid:order_number>/cancel/",
        CancelOrderApi.as_view(),
        name="order-cancel",
    ),
    path(
        "<uuid:order_number>/reorder/",
        ReorderApi.as_view(),
        name="order-reorder",
    ),
    path(
        "admin/<uuid:order_number>/status/",
        AdminOrderStatusApi.as_view(),
        name="admin-order-status",
    ),
]

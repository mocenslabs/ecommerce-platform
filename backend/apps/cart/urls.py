from django.urls import path

from apps.cart.apis.cart import (
    CartDetailApi,
)
from apps.cart.apis.cart_item import (
    CartItemCreateApi,
    CartItemDeleteApi,
    CartItemUpdateApi,
)

urlpatterns = [
    path(
        "",
        CartDetailApi.as_view(),
        name="cart-detail",
    ),
    path(
        "items/",
        CartItemCreateApi.as_view(),
        name="cart-item-create",
    ),
    path(
        "items/<uuid:pk>/update/",
        CartItemUpdateApi.as_view(),
        name="cart-item-update",
    ),
    path(
        "items/<uuid:pk>/delete/",
        CartItemDeleteApi.as_view(),
        name="cart-item-delete",
    ),
]

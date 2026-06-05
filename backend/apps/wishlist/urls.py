from django.urls import path

from apps.wishlist.apis import (
    WishlistApi,
)

urlpatterns = [
    path(
        "",
        WishlistApi.as_view(),
        name="wishlist",
    ),
]

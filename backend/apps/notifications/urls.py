from django.urls import path

from apps.notifications.apis import (
    MarkNotificationAsReadApi,
    NotificationListApi,
    UnreadNotificationCountApi,
)

urlpatterns = [
    path(
        "",
        NotificationListApi.as_view(),
        name="notifications",
    ),
    path(
        "unread-count/",
        UnreadNotificationCountApi.as_view(),
        name="unread-notification-count",
    ),
    path(
        "<uuid:notification_id>/read/",
        MarkNotificationAsReadApi.as_view(),
        name="mark-notification-read",
    ),
]

from rest_framework import serializers

from apps.notifications.models import (
    Notification,
)


class NotificationSerializer(
    serializers.ModelSerializer,
):
    """
    Serialize user notifications.
    """

    class Meta:
        model = Notification

        fields = [
            "id",
            "notification_type",
            "title",
            "message",
            "read",
            "data",
            "created_at",
        ]

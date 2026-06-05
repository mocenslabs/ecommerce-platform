from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.notifications.models import (
    Notification,
)
from apps.notifications.serializers import (
    NotificationSerializer,
)


class NotificationListApi(
    APIView,
):
    """
    List user notifications.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        """
        Return user notifications.
        """

        notifications = Notification.objects.filter(
            user=request.user,
        ).order_by(
            "-created_at",
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(
            serializer.data,
        )


class UnreadNotificationCountApi(
    APIView,
):
    """
    Return unread notifications count.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        """
        Return unread count.
        """

        count = Notification.objects.filter(
            user=request.user,
            read=False,
        ).count()

        return Response(
            {
                "unread_count": count,
            }
        )


class MarkNotificationAsReadApi(
    APIView,
):
    """
    Mark notification as read.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
        notification_id,
    ):
        """
        Mark notification as read.
        """

        notification = get_object_or_404(
            Notification,
            id=notification_id,
            user=request.user,
        )

        notification.read = True

        notification.save(
            update_fields=[
                "read",
            ]
        )

        return Response(
            {
                "success": True,
            }
        )

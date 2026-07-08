from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import (
    Response,
)
from rest_framework.views import (
    APIView,
)

from apps.users.serializers.change_password import (
    ChangePasswordSerializer,
)


class ChangePasswordApi(
    APIView,
):
    """
    Change customer password.
    """

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
    ):
        serializer = ChangePasswordSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        user = request.user

        if not user.check_password(serializer.validated_data["current_password"]):
            return Response(
                {"detail": "Current password is incorrect."},
                status=400,
            )

        user.set_password(serializer.validated_data["new_password"])

        user.save()

        return Response({"detail": "Password updated successfully."})

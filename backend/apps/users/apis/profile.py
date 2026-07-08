from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

from apps.users.serializers.profile import (
    ProfileSerializer,
)


class ProfileApi(
    generics.RetrieveUpdateAPIView,
):
    """
    Customer profile.
    """

    serializer_class = ProfileSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(
        self,
    ):
        return self.request.user

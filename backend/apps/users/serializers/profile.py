from rest_framework import serializers

from apps.users.models import User


class ProfileSerializer(
    serializers.ModelSerializer,
):
    """
    Customer profile serializer.
    """

    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
        ]

        read_only_fields = [
            "id",
            "email",
        ]

from rest_framework import serializers


class UserSerializer(
    serializers.Serializer,
):
    """
    Authenticated user serializer.
    """

    id = serializers.UUIDField(
        read_only=True,
    )

    email = serializers.EmailField(
        read_only=True,
    )

    first_name = serializers.CharField(
        read_only=True,
    )

    last_name = serializers.CharField(
        read_only=True,
    )

    role = serializers.CharField(
        read_only=True,
    )

    is_verified = serializers.BooleanField(
        read_only=True,
    )

from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    """
    Login serializer.
    """

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, attrs):
        """
        Validate credentials.
        """

        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password,
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid credentials.",
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "User is inactive.",
            )

        attrs["user"] = user

        return attrs


class RegisterSerializer(
    serializers.ModelSerializer,
):
    """
    User registration serializer.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User

        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
        ]

    def create(
        self,
        validated_data,
    ):
        """
        Create new user.
        """

        return User.objects.create_user(
            **validated_data,
        )


class UserSerializer(
    serializers.ModelSerializer,
):
    """
    Authenticated user serializer.
    """

    class Meta:
        model = User

        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
        ]

from rest_framework import serializers


class TimestampSerializerMixin(
    serializers.ModelSerializer,
):
    """
    Adds timestamp fields to serializers.
    """

    created_at = serializers.DateTimeField(
        read_only=True,
    )

    updated_at = serializers.DateTimeField(
        read_only=True,
    )

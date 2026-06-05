from django.urls import path

from apps.core.apis.health import (
    HealthCheckApi,
)
from apps.core.apis.readiness import ReadinessApi

urlpatterns = [
    path(
        "health/",
        HealthCheckApi.as_view(),
        name="health",
    ),
    path(
        "readiness/",
        ReadinessApi.as_view(),
        name="readiness",
    ),
]

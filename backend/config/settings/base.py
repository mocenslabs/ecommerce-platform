from datetime import timedelta
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = config(
    "SECRET_KEY",
    default="test-secret-key-for-ci",
)

DEBUG = config(
    "DEBUG",
    cast=bool,
    default=False,
)

ENVIRONMENT = config(
    "ENVIRONMENT",
    default="development",
)


ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda v: [s.strip() for s in v.split(",")],
    default="localhost,127.0.0.1",
)


# =========================================================
# APPLICATIONS
# =========================================================

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_celery_beat",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_extensions",
]

LOCAL_APPS = [
    "apps.core",
    "apps.users",
    "apps.catalog",
    "apps.inventory",
    "apps.cart",
    "apps.orders",
    "apps.payments",
    "apps.discounts",
    "apps.reviews",
    "apps.wishlist",
    "apps.dashboard",
    "apps.notifications",
    "apps.audit",
    "apps.authentication",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "apps.core.middleware.request_id.RequestIdMiddleware",
    "apps.core.middleware.performance.PerformanceLoggingMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# ROOT URLS
# =========================================================

ROOT_URLCONF = "config.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": ("django.template.backends.django.DjangoTemplates"),
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                ("django.template.context_processors.request"),
                ("django.contrib.auth.context_processors.auth"),
                ("django.contrib.messages.context_processors.messages"),
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "config.wsgi.application"


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# =========================================================
# DEFAULTS
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

# =========================================================
# PASSWORD VALIDATORS
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": ("django.contrib.auth.password_validation.MinimumLengthValidator"),
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": ("django.contrib.auth.password_validation.CommonPasswordValidator"),
    },
    {
        "NAME": ("django.contrib.auth.password_validation.NumericPasswordValidator"),
    },
    {
        "NAME": ("apps.core.validators.password.StrongPasswordValidator"),
    },
]
# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        ("rest_framework_simplejwt.authentication.JWTAuthentication"),
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_FILTER_BACKENDS": (
        ("django_filters.rest_framework.DjangoFilterBackend"),
        ("rest_framework.filters.SearchFilter"),
        ("rest_framework.filters.OrderingFilter"),
    ),
    "DEFAULT_PAGINATION_CLASS": ("apps.core.pagination.DefaultPagination"),
    "PAGE_SIZE": 12,
    "DEFAULT_THROTTLE_CLASSES": [
        ("rest_framework.throttling.AnonRateThrottle"),
        ("rest_framework.throttling.UserRateThrottle"),
        ("rest_framework.throttling.ScopedRateThrottle"),
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/hour",
        "user": "1000/hour",
        "login": "10/minute",
        "checkout": "20/minute",
        "webhook": "60/minute",
    },
    "EXCEPTION_HANDLER": ("apps.core.exceptions.handlers.custom_exception_handler"),
    "DEFAULT_PERMISSION_CLASSES": [
        ("rest_framework.permissions.AllowAny"),
    ],
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# =========================================================
# JWT
# =========================================================

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=30,
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        days=7,
    ),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}


# =========================================================
# LOGGING
# =========================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": ("[{asctime}] {levelname} {name} {message}"),
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": ("logging.StreamHandler"),
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": [
            "console",
        ],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propagate": False,
        },
        "apps": {
            "handlers": [
                "console",
            ],
            "level": "INFO",
            "propagate": False,
        },
    },
}


# =========================================================
# CELERY
# =========================================================

CELERY_BROKER_URL = config(
    "CELERY_BROKER_URL",
    default="redis://localhost:6379/0",
)

CELERY_RESULT_BACKEND = config(
    "CELERY_RESULT_BACKEND",
    default="redis://localhost:6379/0",
)

CELERY_ACCEPT_CONTENT = [
    "json",
]

CELERY_TASK_SERIALIZER = "json"

CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = "UTC"


CELERY_TASK_ROUTES = {
    "apps.notifications.tasks.*": {
        "queue": "notifications",
    },
    "apps.orders.tasks.*": {
        "queue": "orders",
    },
    "apps.inventory.tasks.*": {
        "queue": "inventory",
    },
    "apps.cart.tasks.*": {
        "queue": "maintenance",
    },
}


# =========================================================
# EMAIL
# =========================================================

DEFAULT_FROM_EMAIL = "noreply@example.com"


# =========================================================
# CACHE
# =========================================================

CACHES = {
    "default": {
        "BACKEND": ("django.core.cache.backends.redis.RedisCache"),
        "LOCATION": config(
            "REDIS_CACHE_URL",
            default="redis://redis:6379/1",
        ),
    }
}


# =========================================================
# CORS
# =========================================================

CORS_ALLOW_ALL_ORIGINS = True

# ==========================================================
# EMAIL
# ==========================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = "noreply@ecommerce.local"

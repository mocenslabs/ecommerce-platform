from .base import *

# =========================================================
# DATABASE
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# =========================================================
# PASSWORD HASHERS
# =========================================================

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# =========================================================
# CACHE
# =========================================================

CACHES = {
    "default": {
        "BACKEND": ("django.core.cache.backends.locmem.LocMemCache"),
    },
}

# =========================================================
# CELERY
# =========================================================

CELERY_TASK_ALWAYS_EAGER = True

CELERY_TASK_EAGER_PROPAGATES = True

CELERY_BROKER_URL = "memory://"

CELERY_RESULT_BACKEND = "cache+memory://"

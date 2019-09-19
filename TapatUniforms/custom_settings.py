import datetime
import environ

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# False if not in os.environ
DEBUG = env("DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["tapatapi.civilmachines.com"]

CUSTOM_APPS = [
    "drf_user",
    "drf_yasg",
    "order",
    "outlet",
    "school",
    "product",
    "stock_order",
    "rest_framework.authtoken",
]

JWT_AUTH = {
    "JWT_ENCODE_HANDLER": "rest_framework_jwt.utils.jwt_encode_handler",
    "JWT_DECODE_HANDLER": "rest_framework_jwt.utils.jwt_decode_handler",
    "JWT_PAYLOAD_HANDLER": "drf_user.auth.jwt_payload_handler",
    "JWT_PAYLOAD_GET_USER_ID_HANDLER": "rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler",
    "JWT_RESPONSE_PAYLOAD_HANDLER": "rest_framework_jwt.utils.jwt_response_payload_handler",
    "JWT_SECRET_KEY": "update_my_value_in_settings_py",
    "JWT_GET_USER_SECRET_KEY": None,
    "JWT_PUBLIC_KEY": None,
    "JWT_PRIVATE_KEY": None,
    "JWT_ALGORITHM": "HS256",
    "JWT_VERIFY": True,
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LEEWAY": 0,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(weeks=99999),
    "JWT_AUDIENCE": None,
    "JWT_ISSUER": None,
    "JWT_ALLOW_REFRESH": False,
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
    "JWT_AUTH_COOKIE": None,
}

AUTH_USER_MODEL = "drf_user.User"

AUTHENTICATION_BACKENDS = ["drf_user.auth.MultiFieldModelBackend"]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("drfaddons.auth.JSONWebTokenAuthenticationQS",),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}


USER_SETTINGS = {
    "DEFAULT_ACTIVE_STATE": True,
    "OTP": {
        "LENGTH": 5,
        "ALLOWED_CHARS": "1234567890",
        "VALIDATION_ATTEMPTS": 3,
        "SUBJECT": "OTP for Verification",
        "COOLING_PERIOD": 3,
    },
    "MOBILE_VALIDATION": True,
    "EMAIL_VALIDATION": True,
    "REGISTRATION": {
        "SEND_MAIL": False,
        "SEND_MESSAGE": False,
        "MAIL_SUBJECT": "Welcome to DRF-USER",
        "SMS_BODY": "Your account has been created",
        "TEXT_MAIL_BODY": "Your account has been created.",
        "HTML_MAIL_BODY": "Your account has been created.",
    },
}


# Email
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_SSL = env("EMAIL_USE_SSL")
DEFAULT_FROM_EMAIL = EMAIL_FROM = env("DEFAULT_FROM_EMAIL")

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_NAME"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Sentry Integration
sentry_sdk.init(
    dsn="https://5e0a7627fa97442cbe4efca603152e55@sentry.101loop.com/8",
    integrations=[DjangoIntegration()],
)

import datetime

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'drf_user.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': 'update_my_value_in_settings_py',
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_AUTH_COOKIE': None,

}

AUTH_USER_MODEL = 'drf_user.User'

AUTHENTICATION_BACKENDS = [
    'drf_user.auth.MultiFieldModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'drfaddons.auth.JSONWebTokenAuthenticationQS',
    ),
}

USER_SETTINGS = {
    'DEFAULT_ACTIVE_STATE': True,
    'OTP': {
        'LENGTH': 7,
        'ALLOWED_CHARS': '1234567890',
        'VALIDATION_ATTEMPTS': 3,
        'SUBJECT': 'OTP for Verification',
        'COOLING_PERIOD': 3
    },
    'MOBILE_VALIDATION': True,
    'EMAIL_VALIDATION': True,
    'REGISTRATION': {
        'SEND_MAIL': False,
        'SEND_MESSAGE': False,
        'MAIL_SUBJECT': 'Welcome to DRF-USER',
        'SMS_BODY': 'Your account has been created',
        'TEXT_MAIL_BODY': 'Your account has been created.',
        'HTML_MAIL_BODY': 'Your account has been created.'
    }
}

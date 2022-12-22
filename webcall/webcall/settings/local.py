from .base import *
from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-m#^=e(n5t0-^$d45++#w3x5-ad7b87059%eh&h18&7xg05ts4p'

DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webcalldb',
        'USER': 'calladmin',
        'PASSWORD': '0rDaG7PC9z0N',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL SETTINGS

EMAIL_USE_TSL = True
EMAIL_HOST = 'smtp.serviciodecorreo.es'
EMAIL_HOST_USER = get_secret('EMAIL')
EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
EMAIL_PORT = 465

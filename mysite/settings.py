
import os
from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config(
    'SECRET_KEY', default='django-insecure-552!sbp8=_)072$8_#z1u4bw9%z@hb!ci5ml%xu(2j$$ehz4!4')
DEBUG = config('DEBUG', default="True") == "True"

ALLOWED_HOSTS = ["139.59.14.156", "127.0.0.1", "localhost"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blogapp.custom_context_processor.all_category'
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

if DEBUG == True:
    POSTGRES_DB = config('DB_NAME', default=None)  # database name
    # database user password
    POSTGRES_PASSWORD = config('DB_PASSWORD', default=None)
    POSTGRES_USER = config('DB_USERNAME', default=None)  # database username

POSTGRES_READY = (
    POSTGRES_DB is not None
    and POSTGRES_PASSWORD is not None
    and POSTGRES_USER is not None
)

if not POSTGRES_READY:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USERNAME'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


SPACES = config('SPACES', 'FALSE') == 'TRUE'
if SPACES:

    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')

    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }

    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')

    # static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # newly added - media settings
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'mystite.spaces.MediaStorage'

else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'static'

    # newly added - media settings
    MEDIA_URL = "img/"
    MEDIA_ROOT = BASE_DIR/'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

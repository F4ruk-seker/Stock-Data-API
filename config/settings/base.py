"""
Django settings for MyDjangoApp project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from celery.schedules import crontab
from datetime import timedelta
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Application definition
DJANGO_UNFOLD_ADMIN_APPS: list = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
]

INSTALLED_APPS = DJANGO_UNFOLD_ADMIN_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]+[
    # your apps
    'asset',
    'user',
]+[
    # third party app
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_api_key',
    'corsheaders',
    'import_export',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]+[
    # your middleware
]+[
    # third party middleware
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "UPDATE_LAST_LOGIN": True,
}


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATASET_DIR = BASE_DIR / 'dataset'

# CELERY

# Redis broker ayarları
CELERY_BROKER_URL: str = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND: str = env('CELERY_RESULT_BACKEND', default='django-db')

CELERY_TIMEZONE: str = TIME_ZONE  # or your timezone

CELERY_ACCEPT_CONTENT: list = ['json']
CELERY_TASK_SERIALIZER: str = 'json'
CELERY_RESULT_SERIALIZER: str = 'json'
CELERY_BEAT_SCHEDULER: str = 'celery.beat.PersistentScheduler'

CELERY_BEAT_SCHEDULE: dict = {
    'Get Asset Information Every Weekday At 15 Minute Intervals'.lower().replace(' ', '-'): {
        'task': 'asset.tasks.asset_scraper_task.regular_asset_data_acquisition',
        'schedule': crontab(minute='*/15', hour='8-18', day_of_week='1-5'),
    },
    'Get Public Asset Information Every Weekday At 10 Am'.lower().replace(' ', '-'): {
        'task': 'asset.tasks.public_asset_scraper_task.regular_public_asset_data_acquisition',
        'schedule': crontab(hour='7', day_of_week='1-5'),
    },
}


# Asset - Scraper ENV

ASSET_PUBLIC_OFFER_DATA_SOURCE = env('ASSET_PUBLIC_OFFER_DATA_SOURCE')
ASSET_OFFER_DATA_SOURCE = env('ASSET_OFFER_DATA_SOURCE')

from .base import *


DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    f"https://{env('PRODUCT_HOST')}/",
    f"https://{env('PRODUCT_API_HOST')}"
]

CORS_ALLOWED_ORIGINS = [
    f"https://{env('PRODUCT_HOST')}/",
    f"https://{env('PRODUCT_API_HOST')}"
]

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('PGDATABASE'),
        'USER': env('PGUSER'),
        'PASSWORD': env('PGPASSWORD'),
        'HOST': env('PGHOST'),
        'PORT': env('PGPORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles/'

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail kullanıyorsan
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'  # Kendi e-posta adresin
EMAIL_HOST_PASSWORD = 'your_email_password'  # E-posta şifren
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'

raise NotImplementedError('mail settings is not set')

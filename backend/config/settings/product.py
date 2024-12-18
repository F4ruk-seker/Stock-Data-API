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


raise NotImplementedError('mail settings is not set')

sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,  # Performans takibi için
    send_default_pii=True  # Kişisel tanımlayıcı bilgileri (PII) gönder
)

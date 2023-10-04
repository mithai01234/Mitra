"""
Django settings for Mitra project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d428@iu6&#y1@)zrb=1r&d8kd@kq_w2=%%a(l+_o&m1rkck7as'




# Application definition

INSTALLED_APPS = [
     'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mitraapp',
    'rest_framework',
    'corsheaders',
    'registration',
    'videoupload',
    'userlist',
    'report',
    'videolist',
    'statusapp',
    'relationship'
    # 'chatapp'

]
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     # Other settings...
# }

import os
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# this middleware for authentication
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
# ]
MIDDLEWARE = [
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

ROOT_URLCONF = 'Mitra.urls'
CORS_ORIGIN_ALLOW_ALL = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processor.cart_total_amount',

            ],
        },
    },
]
STATIC_URL = 'static/'

WSGI_APPLICATION = 'Mitra.wsgi.application'

# settings.py

CART_SESSION_ID = 'cart'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgresqladmin',
        'PASSWORD': 'Siance@123',
        'HOST': 'sspmitra.postgres.database.azure.com',
        'PORT': '5432',  # The default PostgreSQL port
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Mitra',
#         'USER': 'postgres',
#         'PASSWORD': 'siance',
#         'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
#         'PORT': '5432',          # Leave empty to use the default PostgreSQL port (usually 5432)
#     }
# }
AUTH_USER_MODEL = 'registration.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'














import os
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#DEBUG = True
#ALLOWED_HOSTS = []

DEBUG = True

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#216 219 212 database 221
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server hostname
EMAIL_PORT = 587  # Port for TLS (587 for TLS, 465 for SSL)
EMAIL_USE_TLS = True  # Use TLS encryption
EMAIL_HOST_USER = 'srutee03@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'yswq okhi enmt vgzo'


import os
from storages.backends.azure_storage import AzureStorage

AZURE_ACCOUNT_NAME = 'csg10032002fb0ba2aa'
AZURE_ACCOUNT_KEY = '6ofACEdLTIu0s4CnDRTRmsfrrtGQMC1kCn5Rz4KLx4KWY3ChKUDAqtkSHoccwphTybD+GeuCjrZ7+AStmLP0bw=='
AZURE_CONTAINER = 'filecont'

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

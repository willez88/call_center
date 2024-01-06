"""
Django settings for call_center project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8$7-fbi_7m0(k)rk7n&zwl_il!ys)2@re(44p3_8bttdok=a(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = [
    ('Email Email', 'email@email.com'),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'auditlog',
    'base',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

ROOT_URLCONF = 'call_center.urls'

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

WSGI_APPLICATION = 'call_center.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'call_center',
        'USER': 'admin',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }

    # 'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'call_center',
    #    'USER':'admin',
    #    'PASSWORD':'123',
    #    'HOST':'localhost',
    #    'PORT':'3306',
    #    'OPTIONS': {
    #        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #    }
    # }
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-ve'

LOCALE_NAME = 'es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static/',
)

LOGIN_URL = 'user:login'

LOGIN_REDIRECT_URL = 'base:home'

LOGOUT_REDIRECT_URL = 'user:login'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

if DEBUG:
    # Configuración para entornos de desarrollo
    EMAIL_HOST_USER = 'email@email.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Configuración para entornos de producción
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'email@email.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SERVER_EMAIL = 'email@email.com'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Registra todos los modelos
AUDITLOG_INCLUDE_ALL_MODELS=True

# No registra los datos cargados usando loaddata
AUDITLOG_DISABLE_ON_RAW_SAVE=True

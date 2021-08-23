"""
Django settings for Archivos_Base project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ybot8j&7!0+!*smxizb9*7g3%uwuox0wcte%gph=^w^_6op*or'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '201.184.129.122',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'origin'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'oauth2_provider',
    'dot_restrict_scopes',
    'rest_framework',
    'francapaisa_zonas',
    'francapaisa_inmuebles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Archivos_Base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'Archivos_Base.wsgi.application'

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default_db.sqlite3'),
    },

    'users_db_read': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    },

    'users_db_write': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    },

    'francapaisa_zonas_db_read': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    },

    'francapaisa_zonas_db_write': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    },

    'francapaisa_inmuebles_db_read': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    },

    'francapaisa_inmuebles_db_write': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        'NAME': 'fp_scrapping',
        'USER': 'FrancaPaisa',
        'PASSWORD': 'FP#$tS',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

DATABASE_ROUTERS = [
    'Archivos_Base.routers.AuthProviderRouter.AuthProviderRouter',
    'Archivos_Base.routers.ContentTypesProviderRouter.ContentTypesProviderRouter',
    'Archivos_Base.routers.OAuth2DOTProviderRouter.OAuth2DOTProviderRouter',
    'Archivos_Base.routers.OAuth2DOTRestrictScopesProviderRouter.OAuth2DOTRestrictScopesProviderRouter',
    'Archivos_Base.routers.SessionsProviderRouter.SessionsProviderRouter',
    'Archivos_Base.routers.AdminProviderRouter.AdminProviderRouter',
    'francapaisa_zonas.routers.FrancaPaisaBackendZonasRouter.FrancaPaisaBackendZonasRouter',
    'francapaisa_inmuebles.routers.FrancaPaisaBackendInmueblesRouter.FrancaPaisaBackendInmueblesRouter',
]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en-us', _('English (US)')),
    ('es-co', _('Spanish (Colombia)'))
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static-francapaisa-backend/'

STATIC_ROOT = os.path.join(BASE_DIR, 'Archivos_Base/backend_static')

# Testing database configuration

TEST_RUNNER = 'Archivos_Base.tests.NoDBInitializationTestRunner.NoDBInitializationTestRunner'

# OAuth2 Provider Settings

OAUTH2_PROVIDER_APPLICATION_MODEL = 'dot_restrict_scopes.RestrictedApplication'

OAUTH2_PROVIDER = {
    # List of Available Scopes
    'SCOPES': {
        "default": "Default scope",
        "francapaisa_users_scope": "backend FrancaPaisa Info Usuarios Scope",
        "francapaisa_zonas_scope": "backend FrancaPaisa Zonas Scope",
        "francapaisa_inmuebles_scope": "backend FrancaPaisa Inmuebles Scope",
    },

    # List of Default Scopes
    'DEFAULT_SCOPES': ["default"],

    # Scope Backend Class (To restrict application scopes)
    'SCOPES_BACKEND_CLASS': 'dot_restrict_scopes.scopes.RestrictApplicationScopes',

    # Token Expire Time Settings
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
}

DOT_RESTRICT_SCOPES = {
    'WRAPPED_SCOPES_BACKEND_CLASS': 'oauth2_provider.scopes.SettingsScopes',
}

# CORS Settings

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

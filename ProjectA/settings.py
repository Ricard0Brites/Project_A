"""
Django settings for ProjectA project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from pathlib import Path
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



from ProjectA.Apps import Admin, Core, Client, Store, StoreAnalytics

AdminAppRootDir = Path(Admin.__file__).resolve().parent
CoreAppRootDir = Path(Core.__file__).resolve().parent
ClientAppRootDir = Path(Client.__file__).resolve().parent
StoreAppRootDir = Path(Store.__file__).resolve().parent
StoreAnalyticsAppRootDir = Path(StoreAnalytics.__file__).resolve().parent

if not DEBUG:
    AdminAppRootDir = os.path.join(AdminAppRootDir, 'AdminWebsite\\dist')
    CoreAppRootDir = os.path.join(CoreAppRootDir, 'CoreWebsite\\dist')
    ClientAppRootDir = os.path.join(ClientAppRootDir, 'ClientWebsite\\dist')
    StoreAppRootDir = os.path.join(StoreAppRootDir, 'StoreWebsite\\dist')
    StoreAnalyticsAppRootDir = os.path.join(StoreAnalyticsAppRootDir, 'StoreAnalyticsWebsite\\dist')

# SECURITY WARNING: keep the secret key used in production secret!
from . import Credentials
SECRET_KEY = Credentials.CUSTOM_SECRET_KEY

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#-----------------------------------------------------------------------
    'rest_framework',
#-----------------------------------------------------------------------
    'ProjectA.Apps.Core',
    'ProjectA.Apps.Store',
    'ProjectA.Apps.Admin',
    'ProjectA.Apps.Client',
    'ProjectA.Apps.StoreAnalytics',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProjectA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': 
        [
            AdminAppRootDir,
            CoreAppRootDir,
            ClientAppRootDir,
            StoreAppRootDir,
            StoreAnalyticsAppRootDir,
        ],
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

WSGI_APPLICATION = 'ProjectA.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(AdminAppRootDir, 'assets'),
    os.path.join(CoreAppRootDir, 'assets'),
    os.path.join(ClientAppRootDir, 'assets'),
    os.path.join(StoreAppRootDir, 'assets'),
    os.path.join(StoreAnalyticsAppRootDir, 'assets'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

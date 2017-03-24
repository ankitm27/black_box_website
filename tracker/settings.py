"""
Django settings for tracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*nn#3qm*l$a53yzs5tb8s$ika-nie=cl^j=0zjacix5t0)@6o#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'trackerapp',
    'crispy_forms',
    'pygmaps',
)

TEMPLATE_DIRS = (
    join(BASE_DIR,  'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tracker.urls'

WSGI_APPLICATION = 'tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django_mongodb_engine',
    'NAME': 'tracker',
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': 27017,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

SITE_ID = u'5772a88f3ab7b85f5a9dbae7'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")

STATICFILES_DIRS =(
    os.path.join(BASE_DIR, "static", "our_static"),
)

MEDIA_URL='/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

SITE_ID = u'576fba003ab7b812c601620f'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

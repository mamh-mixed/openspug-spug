"""
# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.

Django settings for spug project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vk0do47)egwzz!uk49%(y3s(fpx4+ha@ugt-hcv&%&d@hwr&p7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'apps.account',
    'apps.host',
    'apps.setting',
    'apps.exec',
    'apps.schedule',
    'apps.monitor',
    'apps.alarm',
    'apps.config',
    'apps.app',
    'apps.deploy',
    'apps.notify',
    'apps.repository',
    'apps.home',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'libs.middleware.AuthenticationMiddleware',
    'libs.middleware.HandleExceptionMiddleware',
]

ROOT_URLCONF = 'spug.urls'

WSGI_APPLICATION = 'spug.wsgi.application'
ASGI_APPLICATION = 'spug.routing.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
            "capacity": 1000,
            "expiry": 120,
        },
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': False,
    },
]

SCHEDULE_KEY = 'spug:schedule'
SCHEDULE_WORKER_KEY = 'spug:schedule:worker'
MONITOR_KEY = 'spug:monitor'
MONITOR_WORKER_KEY = 'spug:monitor:worker'
EXEC_WORKER_KEY = 'spug:exec:worker'
REQUEST_KEY = 'spug:request'
BUILD_KEY = 'spug:build'
REPOS_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'repos')
BUILD_DIR = os.path.join(REPOS_DIR, 'build')

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

AUTHENTICATION_EXCLUDES = (
    '/account/login/',
    '/setting/basic/',
    re.compile('/apis/.*'),
)

SPUG_VERSION = 'v3.1.4'

# override default config
try:
    from spug.overrides import *
except ImportError:
    pass

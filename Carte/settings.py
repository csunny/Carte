"""
Django settings for desgin project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's5i)xb+b(e-@k@y(ghdtsatgeb*@46@h585ln)4k4cpiv#&f31'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Root path of the project
DEPOSITORY_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))

# add project to python path
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'Carts')
sys.path.insert(1, PROJECT_PATH)

# Add app path
APP_PATH = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(1, APP_PATH)

# Add libs to python path
LIB_PATH = os.path.join(PROJECT_ROOT, 'libs')
sys.path.insert(1, LIB_PATH)

# Version of project
PROJECT_VERSION = "v1.0.0"

ALLOWED_HOSTS = ['www.oceanpp.com', '0.0.0.0', '127.0.0.1']

ADMINS = (
    "Magic Chen", 'cfqsunny@163.com'
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'card'
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

ROOT_URLCONF = 'Carte.urls'

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

WSGI_APPLICATION = 'Carte.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'OPTIONS': {
#             'init_command': 'SET default_storage_engine=INNODB',
#         },
#         'NAME': 'design',  # Or path to database file if using sqlite3.
#         'USER': 'root',  # Not used with sqlite3.
#         'PASSWORD': '123456',  # Not used with sqlite3.
#         'HOST': '127.0.0.1',  # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/data/media/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Domain config
DOMAIN_NAME = 'www.oceanpp.com'

ERROR = {
    'SUCC': {'code': '10000', 'msg': 'success'},
    'ERROR': {'code': '10001', 'msg': 'unknown error'},
    'PARA_ERR': {'code': '10002', 'msg': 'form params error'},
    'NOT_EXIST_ERR': {'code': '10003', 'msg': 'record not exist'},
    'PERM_ERR': {'code': '10004', 'msg': 'no permission for this operation'},
    'SYS_ERR': {'code': '10005', 'msg': 'system is busy'},
    'EXIST_ERR': {'code': '10006', 'msg': 'record already exist'},
    'FORBIDDEN': {'code': '10007', 'msg': 'forbidden'},
    'STATE_ERR': {'code': '10011', 'msg': 'status error'},
    'NUM_LIMIT_ERR': {'code': '10013', 'msg': 'exceed the limit num'},
    'OVERFLOW_MAX_LENGTH_ERR': {'code': '10014', 'msg': 'exceed the limit length of content'},
}

# A sample logging configuration.
# more details on how to customize your logging configuration
# See https://docs.djangoproject.com/en/1.8/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },

        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'include_html': True,
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'info_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/info.log',
            'formatter': 'verbose',
        },
        'error_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
            'formatter': 'verbose',
        },
        'task_info_handler': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/task.info.log',
            'formatter': 'verbose',
        },
        'task_error_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/task.error.log',
            'formatter': 'verbose',
        },
        'cron_info_handler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/cron.info.log',
            'formatter': 'verbose',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['info_handler', 'error_handler', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'model.views': {
            'handlers': ['error_handler', 'mail_admins', 'console'],
            'level': 'INFO',
        },
        'django.task': {
            'handlers': ['task_info_handler', 'task_error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
        'celery': {
            'handlers': ['task_info_handler', 'task_error_handler'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

try:
    from settings_local import *
except ImportError:
    pass

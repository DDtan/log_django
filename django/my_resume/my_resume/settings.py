"""
Django settings for my_resume project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'saha^nw@58s818@p3#x4yt_6fm-6))*surjm$ti3+h4)s5839m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'easy_thumbnails',
    'apis',
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

ROOT_URLCONF = 'my_resume.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR),'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app01.global_views.guid_tag',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_resume.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'my_resume',
    'USER': 'xxxxx',
    'PASSWORD': "xxxxx",
    'HOST': '0.0.0.0',
    'PORT': '3306',
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    }
    }
}

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

# LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR),'static'
]
STATIC_ROOT = os.path.join(BASE_DIR,'collect')


MEDIA_ROOT = os.path.join(BASE_DIR,"media")
# 单位：px
THUMB_W = 200
THUMB_H = 311

if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)
MEDIA_URL = "/media/"

# LOG_PATH = os.path.join(BASE_DIR,"log")
# if not os.path.exists(LOG_PATH):
#     os.mkdir(LOG_PATH)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     # formatters：配置日志格式
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
#         },
#         # 对日志信息进行格式化，每个字段对应了日志格式中的一个字段，更多字段参考官网文档
#         'myformat':{
#             'format': '%(asctime)s %(pathname)s -  %(message)s'
#         }
#     },
#     # handlers： 配置日志记录到哪里
#     'handlers': {
#         'default': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             # 'filename': LOG_PATH+'/all.log',     # 日志输出文件
#             'filename': os.path.join(LOG_PATH, 'all.log'),     # 日志输出文件
#             'maxBytes': 1024*1024*5,       # 文件大小
#             'backupCount': 5,              # 备份份数
#             'formatter':'standard',        # 使用哪种formatters日志格式
#         },
#         'app1': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': LOG_PATH + '/app1.log',  # 日志输出文件
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'myformat',  # 使用哪种formatters日志格式
#         },
#         'console':{
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     # loggers: 定义记录器，供程序调用
#     'loggers': {
#         # 名为django的logger会自动记录，其他需要自己调用
#         'django': {
#             'handlers': ['default','console'],
#             'level': 'DEBUG',
#             'propagate': True
#         }
#     }
# }


THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (200, 311), 'crop': True},
    },
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://0.0.0.0:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",
        },
    },
}
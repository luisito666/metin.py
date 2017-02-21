"""
Django settings for metin2 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p)o%-%(m5!wnn*qn^=&xzvobcaf49zm2asdzo0etp%f(z&)r)8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'bootstrapform',
    'django_markdown',
    'apps.varios',
    'apps.account',
    'apps.player',
    'apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'metin2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'metin2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_metin2',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.16.5.11',
        'PORT': '3306',        
    },
    'player': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'player',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.16.5.11',
        'PORT': '3306',  
        'OPTIONS': {'charset': 'utf8mb4'},
        #'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},        
    },
    'account': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'account',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '172.16.5.11',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'" ,}
    },
    
}

DATABASE_ROUTERS = {
                    'apps.player.router.playerRouter',
                    'apps.account.router.AccountRouter',
                    }
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = '/root/metin2/static'

#Capcha
RECAPTCHA_PUBLIC_KEY = '6Ld3vxEUAAAAADfD0zbMEdz961TbnRQafcK9p8IF'
RECAPTCHA_PRIVATE_KEY = '6Ld3vxEUAAAAAJQpERWdmz_mFcTqauY8Mb7oRf1Y'

NOCAPTCHA = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'luispenagos91@gmail.com' 
EMAIL_HOST_PASSWORD = 'N2tgr45psa(Luis)*'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
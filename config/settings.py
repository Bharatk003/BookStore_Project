"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from pathlib import Path
from environs import Env # new


env = Env() # new
env.read_env() # new
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2ix4&byp%q6=2w$jjv_emc)k00j=v54dtpkxxr@x5bi0c^wzi*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG")
ALLOWED_HOSTS = ['192.168.1.104', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [

    ##inbuild apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ##third party apps
    'allauth',
    'allauth.account',
    ##user define apps
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL",
    default="postgres://postgres@db/postgres")
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')), )
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATICFILES_FINDERS = [ # new
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'


LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT =  'home'

 
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend', # new
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # new


ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email' # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new



 
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG")

DEFAULT_FROM_EMAIL = 'admin@bkbookstore.com'
 
 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587   # Usually 587 for TLS or 465 for SSL
# EMAIL_HOST_USER = 'bkbookstore003@gmail.com'
# EMAIL_HOST_PASSWORD = '!@#$QWERasdf'
# EMAIL_USE_TLS = True  # Set it to True if your SMTP server uses TLS


MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))


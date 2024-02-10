"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.7.

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
SECRET_KEY = 'django-insecure-lj8-!l8&w*hn+$nmlc5h7h1x055!y$2=j)p14p%grv8j*4vdtf'

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

    'api',
    'rest_framework',
    'drf_yasg'
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Schema1',
        'USER': 'admin',
        'PASSWORD': '12345678',
        'HOST': 'techit-dashboard.c1puvxyz3nuy.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8',
            'use_unicode': True,
        },
    }
}

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

USE_TZ = True
TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

COMMUNITIES = [
    {
        "id": 1,
        "team_name": "UCB",
        "full_name": "UC Berkeley"
    },
    {
        "id": 2,
        "team_name": "MSU",
        "full_name": "Michigan State University"
    },
    {
        "id": 3,
        "team_name": "DVC",
        "full_name": "Diablo Valley College"
    },
    {
        "id": 4,
        "team_name": "NYU",
        "full_name": "New York University"
    },
    {
        "id": 5,
        "team_name": "GIT",
        "full_name": "Georgia Institute of Technology"
    },
    {
        "id": 6,
        "team_name": "SFC",
        "full_name": "SF city"
    },
    {
        "id": 7,
        "team_name": "UW",
        "full_name": "University of Washington"
    },
    {
        "id": 8,
        "team_name": "GGC",
        "full_name": "Georgia Gwinnett College"
    },
    {
        "id": 9,
        "team_name": "AU",
        "full_name": "Auburn University"
    },
    {
        "id": 10,
        "team_name": "UCLA",
        "full_name": "UC Los Angeles"
    },
    {
        "id": 11,
        "team_name": "CMU",
        "full_name": "Carnegie Mellon University"
    },
    {
        "id": 12,
        "team_name": "EU",
        "full_name": "Emory University"
    },
    {
        "id": 13,
        "team_name": "BU",
        "full_name": "Boston University"
    },
    {
        "id": 14,
        "team_name": "UM",
        "full_name": "Minnesota"
    },
    {
        "id": 15,
        "team_name": "SUNY",
        "full_name": "State university of New York"
    },
    {
        "id": 16,
        "team_name": "UND",
        "full_name": "University of Notre Dame"
    },
    {
        "id": 1,
        "team_name": "UCB",
        "full_name": "UC Berkeley"
    },
    {
        "id": 17,
        "team_name": "UHM",
        "full_name": "University of Hawaii at Manoa"
    },
    {
        "id": 18,
        "team_name": "OCC",
        "full_name": "Orange Coast College"
    },
    {
        "id": 19,
        "team_name": "UF",
        "full_name": "University of Florida"
    },
    {
        "id": 20,
        "team_name": "SU",
        "full_name": "Syracuse University"
    },
    {
        "id": 21,
        "team_name": "OSU",
        "full_name": "Oregon State University"
    },
    {
        "id": 22,
        "team_name": "CSTCC",
        "full_name": "Cincinnati State Technical and Community College"
    },
    {
        "id": 23,
        "team_name": "CSULB",
        "full_name": "California State University, Long Beach"
    },
    {
        "id": 24,
        "team_name": "UCI",
        "full_name": "UC Irvine"
    },
    {
        "id": 25,
        "team_name": "UCSD",
        "full_name": "UC San Diego"
    },
    {
        "id": 26,
        "team_name": "UCR",
        "full_name": "UC Riverside"
    },
    {
        "id": 27,
        "team_name": "SJSU",
        "full_name": "San Jose State University"
    },
    {
        "id": 28,
        "team_name": "UCD",
        "full_name": "UC Davis"
    },
    {
        "id": 29,
        "team_name": "SMB",
        "full_name": "Santa Monica College"
    },
    {
        "id": 30,
        "team_name": "UIUC",
        "full_name": "University of Illinois at Urbana-Champaign"
    },
    {
        "id": 31,
        "team_name": "USC",
        "full_name": "University of Southern California"
    },
    {
        "id": 32,
        "team_name": "UCSB",
        "full_name": "UC Santa Barbara"
    },
    {
        "id": 33,
        "team_name": "CSUSB",
        "full_name": "CSU San Bernardino"
    }
]

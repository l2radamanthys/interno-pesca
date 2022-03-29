from pathlib import Path
import environ
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, True),
    DATABASE_URL=(str, ""),
    ALLOWED_HOSTS=(str, "ALLOWED_HOSTS"),
    MEDIA_ROOT=(str, "media_archivos_locales"),
    CI=(bool, False),
)
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-db$ujpwffu2w^1p+sa+*2=hn(#v@caj^(z_#xuaxbib+7-@sab"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")
ENVIROMENT = env("ENVIROMENT")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(";")
CORS_ORIGIN_WHITELIST = [f"http://{url}" for url in env("ALLOWED_HOSTS").split(";")]
CORS_ORIGIN_WHITELIST += [f"https://{url}" for url in env("ALLOWED_HOSTS").split(";")]
CORS_ORIGIN_WHITELIST += [
    "http://127.0.0.1:4200",
    "http://127.0.0.1:4201",
]
CORS_ORIGIN_WHITELIST.sort()

VERSION = "0.1.0"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "interno",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {}
DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"), conn_max_age=600)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = "static"
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #os.path.join(BASE_DIR, "media_archivos_locales"),
)

MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "media_archivos_locales")
MEDIA_URL = "/media/"

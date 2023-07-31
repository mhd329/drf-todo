"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG") == "True"

if DEBUG:
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = [
        "http://localhost:3000",
    ]
else:
    ALLOWED_HOSTS = [
        "docker-fullstack-app-env.eba-bvt3kqsw.ap-northeast-2.elasticbeanstalk.com",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = [
        "http://frontend:3000",
    ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # library
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "sslserver",
    # apps
    "accounts",
    "todo",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# db 변경 sqlite >>> mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "PORT": os.getenv("MYSQL_PORT"),
        "HOST": os.getenv("MYSQL_HOST"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
"""
현재 정적 파일 관련 서비스를 하지 않는다.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
"""

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# restframework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),  # 허가 : 인증된 사람만 허가
    "DEFAULT_AUTHENTICATION_CLASSES": (  # 인증 : 아래의 클래스로 인증
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        "config.authentication.CustomJWTAuthentication",  # JWTAuthentication을 상속받아 커스텀
    ),
}

# jwt

from datetime import timedelta

SIMPLE_JWT = {
    # 토큰 라이프사이클 관리
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    # 액세스 토큰 발급할때마다 리프레시토큰 갱신 여부
    "ROTATE_REFRESH_TOKENS": False,
    # 기존 리프레시 토큰의 블랙리스트 추가 여부
    "BLACKLIST_AFTER_ROTATION": True,
    # 마지막 로그인 시간 업데이트 여부
    "UPDATE_LAST_LOGIN": True,
    # 서명에 사용할 알고리즘
    "ALGORITHM": "HS256",
    # 서명에 사용할 비밀키
    "SIGNING_KEY": os.getenv("JWT_SECRET_KEY"),
    # 검증에 사용할 공개키 (기본값 공백)
    "VERIFYING_KEY": "",
    # 유저 id 필드 (기본 "id")
    "USER_ID_FIELD": "email",
    # 유저 id 클레임 이름 (기본 "user_id")
    "USER_ID_CLAIM": "email",
}

AUTH_USER_MODEL = "accounts.User"

"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目路径
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cm=ye$p&98g4j(flyp_n93_c!%viw)n^+&9*($c19hi!463s6&'

# SECURITY WARNING: don't run with debug turned on in production!
# 上线后改为false
DEBUG = True

# 允许访问的主机,上线后改为*允许所有
ALLOWED_HOSTS = []

# Application definition
# 注册的App (App就是功能模块)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'app02',
    'app03',
    'app04',
    'app05',
    'app06',
    'blog',
    'static.file',

]

# Django中间件
# from django.middleware.security import SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # request.session下的方法真正的是交由SessionMiddleware操作的
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 前期学习注释该行,否则影响POST请求提交参数
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'app06.mymiddleware.mymdd.MyMiddleware1',
    # 'app06.mymiddleware.mymdd.MyMiddleware2',
]

ROOT_URLCONF = 'mysite.urls'

# HTML文件存放路径配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# 项目指定的数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangolearning',
        'USER': 'djangolearning',
        'PASSWORD': 'djangolearning123.com',
        # 'HOST': '47.xxx.xxx.111',
        # 'PORT': '13306',

        # 验证auth表的扩展
        'HOST': '1.xxx.xxx.195',
        'PORT': '13306',

        'CHARSET': 'utf8'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'  # 类似于访问静态文件的令牌,此时如果你想要访问静态文件,你就必须以static开头

# 静态文件配置,可以配置多个,从上往下加载(手动添加的)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/file/')

]

"""
/static/bootstrap-3.4.1/css/bootstrap.min.css
/static/ ==> 是令牌
再去STATICFILES_DIRS配置的列表中从上往下依次寻找 bootstrap-3.4.1/css/bootstrap.min.css
"""

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

QINIU_ACCESS_KEY = '123'

# auth全局配置:没有登陆跳转到指定的页面
LOGIN_URL = '/app06/auth_login'

AUTH_USER_MODEL = 'app06.UserInfo'

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'server.urls'  # urls.py 에서 링크를 찾는다
STATIC_URL = '/static/'       # Static files (CSS, JavaScript, Images)

# send_mail : Gmail SMTP 서버 활용
# https://www.codingforentrepreneurs.com/blog/use-gmail-for-email-in-django/
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'muyongcctv@gmail.com'
EMAIL_HOST_PASSWORD = 'homecctv$$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',          # shell 을 jupyter 에서 작업 (template 잘 안됨 ㅠㅠ.)
    'books.apps.BooksConfig',     # App이름. apps.py. AppConfig 클래스
    'games.apps.GamesConfig',
    'rest_framework',
]

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ], # Master Template 경로 지정
        'APP_DIRS': True,                                # 개별 APP의 'templates'를 확인
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],},},]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'server.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# # DB 캐시유형 서버를 활용
# CACHES = {
#     'default': {
#         'BACKEND' : 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION' : '127.0.0.1:11211'
#     }
# }
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mse',
        'USER': 'mseuser',
        'PASSWORD': 'msepass',
        'HOST': 'db',
        'PORT': '',
    }
}

DEBUG = True

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = []
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


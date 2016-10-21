ROOT_URLCONF = 'djangorest_alchemy.tests.test_viewsets'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = "4k^rs)v0h5&8l2wiiko0x1^1ss!9fbur8_q%lb60gc&4&l!)us"
ALLOWED_HOSTS = '*'

import django
django.setup()
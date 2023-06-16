from mysite.settings import *
SECRET_KEY = 'django-insecure-80$q%8&#gpa6&t1qwrgpal8v&aa*#p8-n*^#mi=144r_%9=-(s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []
#INSTALLED_APPS = []

#site framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT =BASE_DIR /'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
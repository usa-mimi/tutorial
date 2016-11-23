from .settings import *  # noqa


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tutorial',
        'USER': 'python',
        'PASSWORD': 'python',
        'HOST': 'localhost',
    }
}

STATIC_ROOT = '/home/mnu/public_html/tutorial/static/'

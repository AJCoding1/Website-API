from .base import *
from .base import env

SECRET_KEY = env("SECRET_KEY",  default="django-insecure-63v)2kf)&z#zm%k@ii)j#_x)alqrp8s&*9x!udo@97x3$*+r%j")
DEBUG = True



CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]



EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
EMAIL_PORT = env('EMAIL_PORT')
DEFAULT_FROM_EMAIL = 'ajcoding@gmail.com'
DOMAIN = env('DOMAIN')
SITE_NAME = 'AJCoding'


# ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'UserProfile.CustomUser'  # adjust according to your app name
AUTH_USER_MODEL = 'bookshelf.CustomUser'
AUTH_USER_MODEL = 'bookshelf.CustomUser'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',  # Add your app here
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # type: ignore
    }
}
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

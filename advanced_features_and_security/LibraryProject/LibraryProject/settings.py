import os
from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
DEBUG = False  # Set to False in production
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS


# Authentication
AUTH_USER_MODEL = 'bookshelf.CustomUser'  # Adjust according to your app name

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf', 
    'csp',
]

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # type: ignore
    }
}
# Security settings for HTTPS
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS
SECURE_HSTS_SECONDS = 31536000  # Enforce HSTS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains in the HSTS policy
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS

# Secure cookies
SESSION_COOKIE_SECURE = True  # Ensure session cookies are only transmitted over HTTPS
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only transmitted over HTTPS

# Secure headers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking by denying framing
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent browsers from MIME-sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filtering

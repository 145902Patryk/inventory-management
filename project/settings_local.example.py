DEBUG = True
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # django.db.backends.postgresql
        'NAME': 'db.sqlite3',
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': 'localhost',  # Or address from pg_hba.conf. Not used with sqlite3.
        'PORT': '',  # Not used with sqlite3.
    }
}

CSRF_TRUSTED_ORIGINS = [
    'https://*.0.0.0.0:8000',
    'http://*.0.0.0.0:8000/',
    'https://*.localhost:8000/',
    'http://*.localhost:8000/',
]

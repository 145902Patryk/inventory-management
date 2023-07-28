# Foobar

Django app for managing inventory.

## Installation

Install required packages.

```bash
pip install -r requirements.txt
```

## Setup
1. Rename ``settings_local.example.py`` file to ``settings_local.py`` then configure `DATABASES` and `CSRF_TRUSTED_ORIGINS`.
2. Run migrations.
```bash
python manage.py migrate
```


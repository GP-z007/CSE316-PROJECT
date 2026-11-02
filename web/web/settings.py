"""
Django settings for the SysPulse web project.

SysPulse — Real-Time Process & Resource Monitor

Standalone, minimal Django 5.x configuration. There are intentionally no
imports from legacy analysis frameworks, no external key-value/document
databases, and no optional services — the app runs with Django alone.
"""

import os
from pathlib import Path

# Agent 163eed4: Defines the standalone dashboard project layout.
BASE_DIR = Path(__file__).resolve().parent.parent

# Agent 163eed4: Configures development security and host settings.
SECRET_KEY = "syspulse-dev-secret-key"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Agent 163eed4: Registers only the Django components required by the dashboard.
INSTALLED_APPS = [
    "django.contrib.staticfiles",
]

# Agent 163eed4: Uses the minimal middleware stack for the dashboard.
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

# Agent 163eed4: Allows the dashboard to render its same-origin VNC iframe.
X_FRAME_OPTIONS = "SAMEORIGIN"

# Agent 163eed4: Identifies the dashboard URL and WSGI entry points.
ROOT_URLCONF = "web.urls"
WSGI_APPLICATION = "web.wsgi.application"

# Agent 163eed4: Locates the dashboard templates and their context processors.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.static",
            ],
        },
    },
]

# Agent 163eed4: Keeps SQLite as the local fallback; no external database is needed.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Agent 163eed4: Serves the dashboard's local static assets.
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Agent 163eed4: Sets the dashboard's locale and timezone defaults.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Agent 163eed4: Sends dashboard logs to the console at INFO level.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

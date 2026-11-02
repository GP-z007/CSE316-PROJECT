"""
WSGI config for the SysPulse web project.

This module exposes the WSGI callable as a module-level variable named
``application``. Any WSGI server (runserver, gunicorn, etc.) discovers it
via the ``WSGI_APPLICATION`` setting.
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

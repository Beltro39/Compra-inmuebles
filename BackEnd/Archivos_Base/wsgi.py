"""
WSGI config for Archivos_Base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Default Environment (same as Development Environment)
# os.environ.setdefault ('DJANGO_SETTINGS_MODULE', "Archivos_Base.settings.default")

# Development Environment
os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.dev")

# Test Environment
# os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.test")

# Production Environment
# os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.prod")

application = get_wsgi_application ()



#!/usr/bin/env python

import os
import sys

if __name__ == '__main__':

    # Default Environment (same as Development Environment)
    #    os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'Archivos_Base.settings.default')

    # Development Environment
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.dev")

    # Test Environment
    #    os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.test")

    # Production Environment
    #    os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Archivos_Base.settings.prod")

    try:

        from django.core.management import execute_from_command_line

    except ImportError as exc:

        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

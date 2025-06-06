#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth import get_user_model

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horizweb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if os.environ.get('CREATE_SUPERUSER') == '1':
        User = get_user_model()
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(
                email='admin@example.com',
                username='admin',
                password='admin123'
            )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

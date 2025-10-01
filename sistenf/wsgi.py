"""
WSGI config for sistenf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistenf.settings')


django.setup()
from django.core.management import call_command
call_command('migrate')

from django.core.wsgi import get_wsgi_application

# 👇 Solo estas 3 líneas son nuevas:


application = get_wsgi_application()

"""
WSGI config for fis_scraper_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fis_scraper_backend.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='static/')
application.add_files(root='venv/lib/python3.10/site-packages/rest_framework/static/')

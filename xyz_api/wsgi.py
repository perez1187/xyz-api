"""
WSGI config for xyz_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xyz_api.settings.local") # we have to change in prod
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xyz_api.settings.production") # we have to change in prod

application = get_wsgi_application()

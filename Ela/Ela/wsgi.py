"""
WSGI config for Ela project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling, MediaCling


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ela.settings")

application = Cling(MediaCling(get_wsgi_application()))


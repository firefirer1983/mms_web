"""
WSGI config for mms_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.db import models
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mms_web.settings")

application = get_wsgi_application()


class Moodee(models.Model):
    username = models.CharField(max_length=64)

"""
WSGI config for ltjjc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import ltjjc.settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ltjjc.settings")

sys.path.append('~/ltccj.com/ltjjc/')
sys.path.append('~/ltccj.com/')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

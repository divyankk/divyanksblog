"""
WSGI config for divyanksblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "divyanksblog.divyanksblog.settings")

#application = get_wsgi_application()
import os,sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/Users/admin/Desktop/divyanksblog')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "divyanksblog.divyanksblog.settings")
from dj_static import Cling
application = Cling(get_wsgi_application())

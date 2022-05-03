"""
WSGI config for systempolls project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
##
#from dotenv import load_dotenv
#config = load_dotenv(".env")
#project_folder = os.path.expanduser('~/systempolls')
#load_dotenv(os.path.join(project_folder, 'env'))

##
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'systempolls.settings')

application = get_wsgi_application()

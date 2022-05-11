import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neoexit.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_code.settings')  # Adjust to your settings module

# Get the WSGI application
application = get_wsgi_application()

# Vercel expects the handler to be named `app`
app = application  # This line is important for Vercel

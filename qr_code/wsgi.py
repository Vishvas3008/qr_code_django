import os

# Set the default settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'qr_code.settings'

# Print to verify the environment variable is set
print(os.environ['DJANGO_SETTINGS_MODULE'])

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application

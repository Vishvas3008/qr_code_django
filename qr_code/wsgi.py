import os

from django.core.wsgi import get_wsgi_application

from django.conf import settings
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_code.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))

app = application # added for django vercel
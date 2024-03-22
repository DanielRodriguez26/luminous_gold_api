import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LUMINOUS_AUTHENTICATION_CORE.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    'http': django_asgi_app,
})
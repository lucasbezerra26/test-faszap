import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import fastzap.website.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fastzap.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            fastzap.website.routing.websocket_urlpatterns
        )
    ),
})
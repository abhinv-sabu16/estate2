"""
ASGI config for estate2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import estateapp.routing  # we'll create this next

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "estate2.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Default HTTP protocol
    "websocket": AuthMiddlewareStack(  # Handles authentication for websockets
        URLRouter(
            estateapp.routing.websocket_urlpatterns  # WebSocket routes from our app
        )
    ),
})



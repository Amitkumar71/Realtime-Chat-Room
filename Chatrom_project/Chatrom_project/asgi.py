"""
ASGI config for Chatrom_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from ChatApp import routing
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chatrom_project.settings')

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    )
})
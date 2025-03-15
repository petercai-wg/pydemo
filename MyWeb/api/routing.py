from django.urls import path
from django.urls import re_path

from . import WSConsumers

websocket_urlpatterns = [
    # path("ws/notifications/", WSConsumers.NotificationConsumer.as_asgi()),
    path("ws/chat/<room_name>/", WSConsumers.ChatConsumer.as_asgi()),
]

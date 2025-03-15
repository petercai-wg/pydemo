"""
Add django-channels for websocket demo
allow server to chat with Client, push message to client

ref:  https://github.com/bugbytes-io/django-htmx-websockets/tree/final
https://github.com/veryacademy/YT-Django-Project-Chatroom-Getting-Started


https://channels.readthedocs.io/en/latest/tutorial/index.html

1. python -m pip install  channels[daphne]
Successfully installed Django-5.1.7 asgiref-3.8.1 autobahn-24.4.2 channels-4.2.0 daphne-4.1.2 txaio-23.1.1

2. Add
INSTALLED_APPS = (
    "daphne",

     "channels",

3. MyWeb.asgi.py
define http and websocket ProtocolTypeRouter
and routing for ws

4. Define routing.py for ws handler

5. add CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}} in settings
"""

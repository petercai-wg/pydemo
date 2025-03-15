import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

# class NotificationConsumer(WebsocketConsumer):
#     def connect(self):
#         self.user = self.scope["user"]
#         if not self.user.is_authenticated:
#             self.close()
#             return
#         self.GROUP_NAME = str(self.user)

#         print(
#             f"NotificationConsumer connect {self.GROUP_NAME}, {self.channel_name}  ..."
#         )
#         async_to_sync(self.channel_layer.group_add)(self.GROUP_NAME, self.channel_name)
#         self.accept()

#     def disconnect(self, close_code):
#         print(
#             f"NotificationConsumer disconnect {self.GROUP_NAME}, {self.channel_name}  ..."
#         )
#         if self.user.is_authenticated:
#             async_to_sync(self.channel_layer.group_discard)(
#                 self.GROUP_NAME, self.channel_name
#             )


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            self.close()
            return
        self.GROUP_NAME = str(self.user)

        print(
            f"ChatConsumer connect {self.GROUP_NAME}, adding channel {self.channel_name}  ..."
        )
        async_to_sync(self.channel_layer.group_add)(self.GROUP_NAME, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        print(f"ChatConsumer disconnect {self.GROUP_NAME}, {self.channel_name}  ...")
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        print(f"ChatConsumer receive  {text_data}")

        async_to_sync(self.channel_layer.group_send)(
            self.GROUP_NAME,
            {"type": "chat_reply_message", "message": message, "username": username},
        )

    def chat_reply_message(self, event):
        message = event["message"]
        username = event["username"]
        print(f"ChatConsumer chat_reply_message  {event}")
        self.send(
            text_data=json.dumps(
                {"type": "chat", "message": message, "username": username}
            )
        )

    def logout_message(self, event):
        active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        user_id_list = []
        for session in active_sessions:
            data = session.get_decoded()
            user_id_list.append(data.get("_auth_user_id", None))

        print(f"active users {user_id_list} ")
        # Query all logged in users based on id list
        active_users = User.objects.filter(id__in=user_id_list)
        for u in active_users:
            if u.is_authenticated:
                self.send(
                    text_data=json.dumps(
                        {
                            "type": "chat",
                            "message": "logout",
                            "username": str(u.username),
                        }
                    )
                )

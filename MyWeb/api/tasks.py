# from django.contrib.auth.models import User
# from django.contrib.sessions.models import Session

import time
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def periodic_task():
    while True:
        # print(f"Task executed at {timezone.now()}")
        # active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
        # user_id_list = []
        # for session in active_sessions:
        #     data = session.get_decoded()
        #     user_id_list.append(data.get("_auth_user_id", None))

        # # Query all logged in users based on id list
        # active_users = User.objects.filter(id__in=user_id_list)
        # for u in active_users:
        #     channel_layer = get_channel_layer()
        #     group_name = str(u.username)
        #     async_to_sync(channel_layer.group_send)(
        #         group_name,
        #         {
        #             "type": "chat_reply_message",
        #             "message": "logout",
        #             "username": str(u.username),
        #         },
        #     )

        time.sleep(1 * 60)  # Run every 5 minutes

        channel_layer = get_channel_layer()
        group_name = "peter"

        print(f"periodic_task send chat to {group_name} at {datetime.datetime.now()}")
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "logout_message",
                "message": "logout",
                "username": group_name,
            },
        )

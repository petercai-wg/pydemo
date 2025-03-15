from django.apps import AppConfig

import threading
import time
from django.utils import timezone


def periodic_task():
    while True:
        print(f"Task executed at {timezone.now()}")
        time.sleep(60)  # Run every 60 seconds


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        if not hasattr(self, "_task_started"):
            self._task_started = True
            threading.Thread(target=periodic_task, daemon=True).start()

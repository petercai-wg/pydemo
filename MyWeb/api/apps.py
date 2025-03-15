from django.apps import AppConfig

import threading

from .tasks import periodic_task


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        if not hasattr(self, "_task_started"):
            self._task_started = True
            threading.Thread(target=periodic_task, daemon=True).start()

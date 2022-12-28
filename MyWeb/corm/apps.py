from django.apps import AppConfig
from django.db.models.signals import post_save


class CormConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "corm"

    def ready(self) -> None:
        import corm.signals

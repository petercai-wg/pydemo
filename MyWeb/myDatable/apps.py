from django.apps import AppConfig

# https://tutorial101.blogspot.com/2020/04/django-crud-create-read-update-delete.html
##


class MydatableConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myDatable"

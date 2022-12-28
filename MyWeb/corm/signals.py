from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Report


@receiver(post_save, sender=Report)
def db_save_receiver(sender,  instance, created, **kwargs):
    print(f"db_save_receiver {instance}  saved  {created} ")

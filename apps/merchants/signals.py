# your_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Merchant

@receiver(post_save, sender=User)
def create_merchant(sender, instance, created, **kwargs):
    """
    Signal handler to create a Merchant when a new User is created.
    """
    if created:
        Merchant.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_merchant(sender, instance, **kwargs):
    """
    Signal handler to save the Merchant when the User is saved.
    """
    instance.merchant.save()

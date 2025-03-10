from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def set_user_to_active(sender, instance, created, **kwargs):
    if created:
        instance.is_active = True
        instance.save()
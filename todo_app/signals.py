from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Post, UpdatedPosts

from threading import Thread

print("SIGNALLLL")


@receiver(post_save, sender=Post, dispatch_uid="start_task")
def start_task(sender, instance, created, **kwargs):
    if created:
        # UpdatedPosts.objects.create(post_id=instance.id, text=instance.text, desc=instance.desc, version=instance.version)
        pass
    else:
       pass
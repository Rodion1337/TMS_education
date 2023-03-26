from .models import Games, Categories, Comments
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
import time
from django.core import serializers
from celery import shared_task
from better_profanity import profanity



@shared_task()
def censored_comment_form(instance):
    from better_profanity import profanity
    import time
    time.sleep(10)
    instance.title=profanity.censor(instance.title)
    instance.content=profanity.censor(instance.content)
    instance.save()
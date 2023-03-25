import time
from django.core import serializers
from celery import shared_task



@shared_task()
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object
    censored_text = profanity.censor(instance.text)
    time.sleep(5)
    instance.text = censored_text
    instance.save()
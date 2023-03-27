from .models import Games, Categories, Comments
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
import time
from django.core.serializers import deserialize
from celery import shared_task
from better_profanity import profanity
import time
import logging
from DjangoProject.settings import BASE_DIR
import os

profanity.load_censor_words()

@shared_task()
def censored_comment_form(instance):
    instance_deserialize = list(deserialize('json', instance))[0].object
    time.sleep(10)
    instance_deserialize.title=profanity.censor(instance_deserialize.title)
    instance_deserialize.content=profanity.censor(instance_deserialize.content)
    instance_deserialize.save()

@shared_task()
def logger_task(msg):
    logger = logging.getLogger('HW34')
    logger.setLevel(logging.INFO)
    # log_file = str([os.path.join(BASE_DIR, 'log.log')])
    logger_handler = logging.FileHandler('log.log')
    logger_handler.setLevel(logging.INFO)
    logger_formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)
    logger.info(msg=msg)
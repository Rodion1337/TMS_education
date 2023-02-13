from .models import games
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, pre_save

@receiver(post_save, sender = games)
def game_amount_up(sender, instance, created, **kwargs):
    instance = instance.category
    if created:
        instance.game_amount += 1
        instance.save()
    if instance.slug == 'null':
        x = instance.name
        instance.slug = '_'.join(x.lower().split(' '))
        instance.save()


@receiver(pre_delete, sender = games)
def game_amount_up(sender, instance, **kwargs):
    instance = instance.category
    instance.game_amount -= 1
    instance.save()
        
# @receiver(post_save, sender = games)   
# def upd_slug(sender, instance, **kwargs):
#     if instance.slug == 'null':
#         x = instance.name
#         instance.slug = '_'.join(x.lower().split(' '))
#         instance.save()
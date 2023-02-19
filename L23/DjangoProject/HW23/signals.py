from .models import Games, Categories
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete, pre_save
from string import punctuation, ascii_letters, digits

@receiver(post_save, sender = Games)
def game_amount_up(sender, instance, created, **kwargs):
    instance = instance.category
    if created:
        instance.game_amount += 1
        instance.save()


@receiver(pre_delete, sender = Games)
def game_amount_up(sender, instance, **kwargs):
    instance = instance.category
    instance.game_amount -= 1
    instance.save()
        
@receiver(pre_save, sender = Categories)
@receiver(pre_save, sender = Games)
def upd_slug(sender, instance, **kwargs):
    if instance.slug == None:
        x = instance.name
        dic = {'Ь':'', 'ь':'', 'Ъ':'', 'ъ':'', 'А':'A', 'а':'a', 'Б':'B', 'б':'b', 'В':'V', 'в':'v',
            'Г':'G', 'г':'g', 'Д':'D', 'д':'d', 'Е':'E', 'е':'e', 'Ё':'Yo', 'ё':'yo', 'Ж':'Zh', 'ж':'zh',
            'З':'Z', 'з':'z', 'И':'I', 'и':'i', 'Й':'Y', 'й':'y', 'К':'K', 'к':'k', 'Л':'L', 'л':'l',
            'М':'M', 'м':'m', 'Н':'N', 'н':'n', 'О':'O', 'о':'o', 'П':'P', 'п':'p', 'Р':'R', 'р':'r', 
            'С':'S', 'с':'s', 'Т':'T', 'т':'t', 'У':'U', 'у':'u', 'Ф':'F', 'ф':'f', 'Х':'H', 'х':'h',
            'Ц':'Ts', 'ц':'ts', 'Ч':'Ch', 'ч':'ch', 'Ш':'Sh', 'ш':'sh', 'Щ':'Sch', 'щ':'sch', 'Ы':'Yi',
            'ы':'yi', 'Э':'E', 'э':'e', 'Ю':'Yu', 'ю':'yu', 'Я':'Ya', 'я':'ya', ' ':'_'}
        name_slug = ''
        text_free = ascii_letters + digits
        for i in instance.name:
            if i in text_free:
                name_slug += i
            elif i in punctuation:
                pass
            else:
                name_slug += str(dic[i])
        instance.slug = name_slug.lower()
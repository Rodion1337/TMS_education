from django.db import models
from func.validate import Validator

# Create your models here.
class Bd(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    price =models.FloatField(null=True, blank=True)
    publisher = models.DateTimeField(auto_now_add=True, db_index=True)
    
class user(models.Model):
    login = models.CharField(max_length=150, verbose_name='Ник', validators=[Validator.validate_login])
    firstname = models.CharField(max_length=150, verbose_name='Имя')
    lastname = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.CharField(max_length=150, verbose_name='E-mail', validators=[Validator.validate_email])
    password = models.CharField(max_length=150, verbose_name='Пароль', validators=[Validator.validate_password])
    
class post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(null=True, blank=True, verbose_name='Статья')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    author = user.nickname

class category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='')
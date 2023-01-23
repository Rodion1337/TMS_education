from django.db import models
from func.validate import Validator

# Create your models here.
class Bd(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price =models.FloatField(null=True, blank=True, verbose_name='Цена')
    publisher = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-publisher']

class user(models.Model):
    login = models.CharField(max_length=150, verbose_name='Ник', validators=[Validator.validate_login])
    firstname = models.CharField(max_length=150, verbose_name='Имя')
    lastname = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.CharField(max_length=150, verbose_name='E-mail', validators=[Validator.validate_email])
    password = models.CharField(max_length=150, verbose_name='Пароль', validators=[Validator.validate_password])
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['login']

class post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(verbose_name='Статья')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    author = models.ForeignKey('user', verbose_name=("Автор"), on_delete=models.SET_DEFAULT, default = 'user delete')
    
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-published']

class category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(null=True, blank=True, verbose_name='')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']
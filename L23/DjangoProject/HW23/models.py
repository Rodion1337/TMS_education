from django.db import models

# Create your models here.

class ShopInfoMixin(models.Model):
    is_active = models.fields.BooleanField(verbose_name = 'Активация', default = False)
    slug = models.SlugField(verbose_name = "Адрес", blank = True, null = True)
    
    class Meta:
        abstract = True

class GamesDev(models.Model):
    nameDev = models.CharField(verbose_name='Разработчик', max_length=50, db_index=True)
    description = models.TextField(verbose_name='Описание',blank=True, null=True)
    
    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
        ordering = ['nameDev']
    
    def __str__(self) -> str:
        return self.nameDev

class Categories(ShopInfoMixin):
    title = models.CharField(verbose_name = 'Категория', max_length = 50)
    description = models.TextField(verbose_name = ("Описание"))
    game_amount = models.IntegerField(verbose_name = 'Игр в категории', default = 0)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
    
    def __str__(self) -> str:
        return self.title

class Status(models.Model):
    status_name = models.CharField(verbose_name = 'Статус', max_length = 50)
    
    def __str__(self) -> str:
        return self.status_name

class Games(ShopInfoMixin):
    name = models.CharField(max_length=150, verbose_name='Игра', db_index=True)
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    upd_date = models.DateField(auto_now=True, verbose_name='Дата обновления')
    release_date = models.DateField(verbose_name='Дата релиза')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name = 'Цена', default = 0)
    gameDev = models.ForeignKey(GamesDev, verbose_name = 'Издатель', on_delete = models.PROTECT)
    category = models.ForeignKey(Categories, verbose_name = 'Категория', on_delete = models.PROTECT)
    description = models.TextField(verbose_name = 'Описание игры')
    game_image = models.ImageField(verbose_name = 'Логотип игры', upload_to = 'images', height_field=None, width_field=None, max_length=None)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete = models.PROTECT, default = 1)
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name
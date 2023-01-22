from django.db import models

# Create your models here.
class Bd(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(null=True, blank=True)
    price =models.FloatField(null=True, blank=True)
    publisher = models.DateTimeField(auto_now_add=True, db_index=True)
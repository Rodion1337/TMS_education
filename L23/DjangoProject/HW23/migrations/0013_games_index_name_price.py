# Generated by Django 4.1.6 on 2023-02-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HW23', '0012_remove_games_is_active_game'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='games',
            index=models.Index(fields=['name', 'price'], name='index_name_price'),
        ),
    ]

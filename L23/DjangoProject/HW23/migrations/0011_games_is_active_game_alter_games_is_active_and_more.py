# Generated by Django 4.1.6 on 2023-02-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HW23', '0010_remove_games_is_active_game_remove_games_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='is_active_game',
            field=models.BooleanField(default=False, verbose_name='Активация'),
        ),
        migrations.AlterField(
            model_name='games',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активация'),
        ),
        migrations.AlterField(
            model_name='games',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Адрес'),
        ),
    ]
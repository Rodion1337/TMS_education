# Generated by Django 4.1.5 on 2023-01-29 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='user delete', on_delete=django.db.models.deletion.SET_DEFAULT, to='bboard.user', verbose_name='Автор'),
        ),
    ]

    # operations = [
    #     migrations.AlterField(
    #         model_name='post',
    #         name='author',
    #         field=models.ForeignKey(default=user_delete_name(), on_delete=django.db.models.deletion.SET_DEFAULT, to='bboard.user', verbose_name='Автор'),
    #     ),
    # ]
    
    # def user_delete_name():
        
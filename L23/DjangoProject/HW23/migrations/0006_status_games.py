# Generated by Django 4.1.6 on 2023-02-12 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HW23', '0005_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='HW23.status', verbose_name='Статус'),
        ),
    ]

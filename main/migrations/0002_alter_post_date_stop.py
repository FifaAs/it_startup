# Generated by Django 4.2.16 on 2024-11-16 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Date_Stop',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Закрытие регистрации'),
        ),
    ]

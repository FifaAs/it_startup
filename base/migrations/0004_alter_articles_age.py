# Generated by Django 4.2.16 on 2024-11-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_articles_nameclub_articles_namenews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
    ]

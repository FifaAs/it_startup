# Generated by Django 4.2.16 on 2024-11-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_articles_options_alter_articles_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='NameClub',
            field=models.CharField(blank=True, max_length=50, verbose_name='Клуб'),
        ),
        migrations.AddField(
            model_name='articles',
            name='NameNews',
            field=models.CharField(blank=True, max_length=50, verbose_name='Событие'),
        ),
    ]
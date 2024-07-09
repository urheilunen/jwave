# Generated by Django 5.0.6 on 2024-07-08 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwavesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subscribants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Подписан(а) на'),
        ),
    ]
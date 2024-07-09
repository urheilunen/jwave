from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(blank=True, null=True, max_length=10, verbose_name='Пол')
    city = models.TextField(blank=True, null=True, verbose_name='Город')
    relationship_status = models.CharField(max_length=10, blank=True, null=True, verbose_name='Статус')
    subscribants = models.ManyToManyField('self', symmetrical=False, verbose_name='Подписан(а) на')

    
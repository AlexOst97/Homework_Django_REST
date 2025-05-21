from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email =  models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/image',blank=True, null=True, verbose_name='Изображение')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
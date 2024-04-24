from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderators')


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='Имя', unique=True, **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта', **NULLABLE)

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return f'{self.username}{self.role}'

from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class BaseContacts(models.Model):
    name_contact = models.CharField(max_length=100, default='', verbose_name='Имя контакта')
    email = models.EmailField(**NULLABLE)
    country = models.CharField(max_length=100, default='', verbose_name='Страна')
    city = models.CharField(max_length=100, default='', verbose_name='Город')
    street = models.CharField(max_length=100, default='', verbose_name='Улица')
    house_number = models.CharField(max_length=100, default=0, verbose_name='Номер дома')

    def __str__(self):
        return self.name_contact

    class Meta:
        abstract = True


class BaseProduct(models.Model):
    name_product = models.CharField(max_length=100, verbose_name='Имя продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date_launch = models.DateField(verbose_name='Дата выхода продукта на рынок')
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                                           verbose_name='Задолженность перед поставщиком')
    creation_date = models.DateTimeField(default=timezone.now, verbose_name='Время создания')

    def __str__(self):
        return self.name_product

    class Meta:
        abstract = True

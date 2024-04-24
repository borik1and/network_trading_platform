from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Factory_contacts(models.Model):
    factory_name = models.CharField(max_length=100, default='', verbose_name='Название завода')
    email = models.EmailField(**NULLABLE)
    country = models.CharField(max_length=100, default='', verbose_name='страна')
    city = models.CharField(max_length=100, default='', verbose_name='город')
    street = models.CharField(max_length=100, default='', verbose_name='улица')
    house_number = models.CharField(max_length=100, default=0, verbose_name='номер дома')

    def __str__(self):
        return self.factory_name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Factory_product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя продукта')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date_launch = models.DateField(verbose_name='дата выхода продукта на рынок')
    provider = models.ForeignKey(Factory_contacts, verbose_name='Поставщик', on_delete=models.CASCADE)
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                                           verbose_name='Задолженность перед поставщиком')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

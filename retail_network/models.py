from base.models import BaseContacts, BaseProduct
from django.db import models

from factory.models import Factory

NULLABLE = {'blank': True, 'null': True}


class RetailNetwork(BaseContacts, BaseProduct):
    provider = models.ForeignKey(Factory, verbose_name='Поставщик', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'розничная сеть'
        verbose_name_plural = 'розничные сети'

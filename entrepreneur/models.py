from base.models import BaseContacts, BaseProduct
from django.db import models

from factory.models import Factory

NULLABLE = {'blank': True, 'null': True}


class Entrepreneur(BaseContacts, BaseProduct):
    provider = models.ForeignKey(Factory, verbose_name='Поставщик', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'индивидуальный предприниматель'
        verbose_name_plural = 'индивидуальный предприниматели'

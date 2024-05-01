from base.models import BaseContacts, BaseProduct
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Factory(BaseContacts, BaseProduct):
    provider = models.ForeignKey('entrepreneur.Entrepreneur', verbose_name='Поставщик', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'

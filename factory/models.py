from base.models import BaseContacts, BaseProduct

NULLABLE = {'blank': True, 'null': True}


class Factory(BaseContacts, BaseProduct):
    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'

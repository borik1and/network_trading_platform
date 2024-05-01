from django.contrib import admin
from django.utils.html import format_html

from entrepreneur.models import Entrepreneur


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Entrepreneur)
class EntrepreneurContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name_contact', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model', 'date_launch',
        'creation_date', 'debt_to_supplier', 'provider'
    )

    list_filter = ('country',)

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                return format_html('<a href="{0}/{1}/">{1}</a>',
                                   '/admin/entrepreneur/entrepreneur', provider)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'Поставщик'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]  # Добавляем действие к списку действий модели Entrepreneur_product

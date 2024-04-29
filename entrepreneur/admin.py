from django.contrib import admin
from django.utils.html import format_html
from entrepreneur.models import Entrepreneur_contacts, Entrepreneur_product


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Entrepreneur_contacts)
class EntrepreneurContactsAdmin(admin.ModelAdmin):
    list_display = ('retail_network_name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country',)


@admin.register(Entrepreneur_product)
class EntrepreneurProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date', 'debt_to_supplier')

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                return format_html('<a href="{0}/{1}/">{1}</a>',
                                   '/admin/entrepreneur/entrepreneur-product', provider)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'Поставщик'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]  # Добавляем действие к списку действий модели Entrepreneur_product

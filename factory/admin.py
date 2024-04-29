from django.contrib import admin
from factory.models import Factory_contacts, Factory_product
from django.utils.html import format_html


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Factory_contacts)
class FactoryContactsAdmin(admin.ModelAdmin):
    list_display = ('factory_name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country',)


@admin.register(Factory_product)
class FactoryProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date', 'debt_to_supplier')

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                return format_html('<a href="{0}/{1}/">{1}</a>',
                                   '/admin/factory/factory-product', provider)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'Поставщик'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]

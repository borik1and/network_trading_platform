from django.contrib import admin
from factory.models import Factory
from django.utils.html import format_html


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Factory)
class FactoryProductAdmin(admin.ModelAdmin):
    list_display = (
        'name_contact', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model', 'date_launch',
        'creation_date', 'debt_to_supplier', 'provider'
    )

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                return format_html('<a href="{0}/{1}/">{1}</a>',
                                   '/admin/factory/factory', provider)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'Поставщик'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]

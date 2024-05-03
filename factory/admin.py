from django.contrib import admin
from factory.models import Factory
from django.utils.html import format_html
from rest_framework.reverse import reverse

def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Factory)
class FactoryProductAdmin(admin.ModelAdmin):
    list_display = (
        'name_contact', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model', 'date_launch',
        'creation_date', 'debt_to_supplier',
    )

    list_filter = ('country',)



from django.contrib import admin
from django.utils.html import format_html
from rest_framework.reverse import reverse

from retail_network.models import RetailNetwork


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'name_contact', 'email', 'country', 'city', 'street', 'house_number', 'name_product', 'model', 'date_launch',
        'creation_date', 'debt_to_supplier', 'provider'
    )
    list_filter = ('country',)

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                url = reverse("admin:factory_factory_change", args=[provider.id])
                return format_html('<a href="{}">{}</a>', url, provider.name_contact)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'ссылка на «Поставщика'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]

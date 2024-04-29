from django.contrib import admin
from django.utils.html import format_html
from retail_network.models import Retail_network_contacts, Retail_network_product


def clear_debt_to_supplier(self, request, queryset):
    queryset.update(debt_to_supplier=0)


clear_debt_to_supplier.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Retail_network_contacts)
class RetailNetworkContactsAdmin(admin.ModelAdmin):
    list_display = ('retail_network_name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country',)


@admin.register(Retail_network_product)
class RetailNetworkProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date', 'debt_to_supplier')

    def link_to_provider(self, obj):
        try:
            provider = obj.provider
            if provider:
                return format_html('<a href="{0}/{1}/">{1}</a>',
                                   '/admin/retail_network/retail-network-product', provider)
        except Exception as e:
            pass
        return None

    link_to_provider.short_description = 'Поставщик'
    link_to_provider.allow_tags = True

    actions = [clear_debt_to_supplier]

from django.contrib import admin

from retail_network.models import Retail_network_contacts, Retail_network_product


@admin.register(Retail_network_contacts)
class RetailNetworkContactsAdmin(admin.ModelAdmin):
    list_display = ('retail_network_name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Retail_network_product)
class RetailNetworkProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date')
from django.contrib import admin

from entrepreneur.models import Entrepreneur_contacts, Entrepreneur_product


@admin.register(Entrepreneur_contacts)
class EntrepreneurContactsAdmin(admin.ModelAdmin):
    list_display = ('retail_network_name', 'email', 'country', 'city', 'street', 'house_number')


@admin.register(Entrepreneur_product)
class EntrepreneurProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date')

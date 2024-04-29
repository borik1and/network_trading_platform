from django.contrib import admin
from factory.models import Factory_contacts, Factory_product


@admin.register(Factory_contacts)
class FactoryContactsAdmin(admin.ModelAdmin):
    list_display = ('factory_name', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('country',)


@admin.register(Factory_product)
class FactoryProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_launch', 'provider', 'creation_date')

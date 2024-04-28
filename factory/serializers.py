from rest_framework import serializers

from factory.models import Factory_contacts, Factory_product


class FactoryContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory_contacts
        fields = '__all__'


class FactoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory_product
        fields = '__all__'

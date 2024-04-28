from rest_framework import serializers

from entrepreneur.models import Entrepreneur_contacts, Entrepreneur_product


class EntrepreneurContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur_contacts
        fields = '__all__'


class EntrepreneurProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur_product
        fields = '__all__'

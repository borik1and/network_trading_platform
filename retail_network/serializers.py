from rest_framework import serializers
from retail_network.models import Retail_network_contacts, Retail_network_product


class RetailNetworkContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_network_contacts
        fields = '__all__'


class RetailNetworkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_network_product
        fields = '__all__'

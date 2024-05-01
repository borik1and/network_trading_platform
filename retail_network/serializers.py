from rest_framework import serializers
from retail_network.models import RetailNetwork


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        exclude = ['debt_to_supplier']

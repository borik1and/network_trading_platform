from rest_framework import serializers

from entrepreneur.models import Entrepreneur


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        exclude = ['debt_to_supplier']






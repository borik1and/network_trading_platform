from rest_framework import serializers

from factory.models import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        exclude = ['debt_to_supplier']

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from entrepreneur.permissions import IsActiveEmployee
from factory.models import Factory_contacts, Factory_product
from factory.serializers import FactoryContactsSerializer, FactoryProductSerializer


class FactoryContactsViewSet(viewsets.ModelViewSet):
    serializer_class = FactoryContactsSerializer
    queryset = Factory_contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]


class FactoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = FactoryProductSerializer
    queryset = Factory_product.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]

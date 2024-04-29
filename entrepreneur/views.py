from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from entrepreneur.models import Entrepreneur_contacts, Entrepreneur_product
from entrepreneur.permissions import IsActiveEmployee
from entrepreneur.serializers import EntrepreneurContactsSerializer, EntrepreneurProductSerializer


class Entrepreneur_contactsViewSet(viewsets.ModelViewSet):
    serializer_class = EntrepreneurContactsSerializer
    queryset = Entrepreneur_contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]


class Entrepreneur_productViewSet(viewsets.ModelViewSet):
    serializer_class = EntrepreneurProductSerializer
    queryset = Entrepreneur_product.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]

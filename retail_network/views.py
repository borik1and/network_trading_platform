from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from entrepreneur.permissions import IsActiveEmployee
from retail_network.models import Retail_network_contacts, Retail_network_product
from retail_network.serializers import RetailNetworkContactsSerializer, RetailNetworkProductSerializer


class RetailNetworkContactsViewSet(viewsets.ModelViewSet):
    serializer_class = RetailNetworkContactsSerializer
    queryset = Retail_network_contacts.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]


class RetailNetworkProductViewSet(viewsets.ModelViewSet):
    serializer_class = RetailNetworkProductSerializer
    queryset = Retail_network_product.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]

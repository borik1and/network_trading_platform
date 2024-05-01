from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from entrepreneur.permissions import IsActiveEmployee
from retail_network.models import RetailNetwork
from retail_network.serializers import RetailNetworkSerializer


class RetailNetworkViewSet(viewsets.ModelViewSet):
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]

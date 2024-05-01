from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from entrepreneur.permissions import IsActiveEmployee
from factory.models import Factory
from factory.serializers import FactorySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    serializer_class = FactorySerializer
    queryset = Factory.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]

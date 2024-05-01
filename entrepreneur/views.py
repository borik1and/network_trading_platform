from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from entrepreneur.models import Entrepreneur
from entrepreneur.permissions import IsActiveEmployee
from entrepreneur.serializers import EntrepreneurSerializer


class EntrepreneurViewSet(viewsets.ModelViewSet):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, IsActiveEmployee]


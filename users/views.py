from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import UserSerializer
from users.models import User
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action in ['create', 'login']:  # Разрешаем только для create и login
            self.permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:  # Запрещаем для update, partial_update и destroy
            self.permission_classes = [IsAuthenticated]
        return super(UserViewSet, self).get_permissions()

    @action(detail=False, methods=['post'])
    def login(self, request):
        # код для входа пользователя
        return Response("Login Successful")

    def create(self, request, *args, **kwargs):
        # код для создания нового пользователя
        return super(UserViewSet, self).create(request, *args, **kwargs)

from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """
    Пользовательский класс разрешений, который проверяет, является ли пользователь активным сотрудником.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь аутентифицированным и активным сотрудником
        return request.user.is_authenticated and request.user.is_active

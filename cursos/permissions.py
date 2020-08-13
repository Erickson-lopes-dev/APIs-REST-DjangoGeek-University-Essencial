from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # se o método for DELETE
        if request.method == 'DELETE':
            # verifica se é um user usuario que esta pedindo
            if request.user.is_superuser:
                return True
            return False
        return True

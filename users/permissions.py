from rest_framework import permissions


class IsModerators(permissions.BasePermission):
    """ Проверка пользователя. Является ли модератором """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderators").exists()


class IsOwners(permissions.BasePermission):
    """ Проверка пользователя. Является ли владельцем """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
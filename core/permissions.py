from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Projects have owner, tasks have project.owner
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'project'):
            return obj.project.owner == request.user
        return False

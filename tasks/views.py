from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(project__owner=self.request.user)

        project_id = self.request.query_params.get("project")
        status = self.request.query_params.get("status")

        if project_id:
            queryset = queryset.filter(project_id=project_id)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

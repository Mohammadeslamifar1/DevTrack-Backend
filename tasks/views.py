from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from core.permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['priority', 'due_date', 'created_at']

    def get_queryset(self):
        # only tasks that belong to projects owned by the user
        return Task.objects.filter(project__owner=self.request.user)

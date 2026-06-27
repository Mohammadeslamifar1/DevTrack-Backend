from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["status", "priority", "project"]
    search_fields = ["title", "description"]
    ordering_fields = ["priority", "due_date", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)

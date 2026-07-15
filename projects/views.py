from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tasks.models import Task

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def dashboard_stats(request):
    user = request.user

    projects = Project.objects.filter(owner=user)
    tasks = Task.objects.filter(project__owner=user)

    total_projects = projects.count()
    total_tasks = tasks.count()

    status_counts = {
        "todo": tasks.filter(status="todo").count(),
        "in_progress": tasks.filter(status="in_progress").count(),
        "done": tasks.filter(status="done").count(),
    }

    return Response({
        "total_projects": total_projects,
        "total_tasks": total_tasks,
        "status_counts": status_counts,
    })


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()

    def get_queryset(self):
        # Only return projects owned by the logged-in user
        user = self.request.user
        return Project.objects.filter(owner=user)

    serializer_class = ProjectSerializer

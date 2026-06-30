from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Project
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

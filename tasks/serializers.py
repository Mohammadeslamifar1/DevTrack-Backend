from rest_framework import serializers
from django.utils import timezone
from django.apps import apps

# Try to get the Project model from the app registry.
# If the registry isn't ready (during initial migrations), Project will be None.
try:
    Project = apps.get_model('projects', 'Project')
except Exception:
    Project = None


class TaskSerializer(serializers.ModelSerializer):
    # If Project is available, provide a real queryset.
    # If not, make the field read_only to satisfy DRF during migrations.
    if Project:
        project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    else:
        project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = apps.get_model('tasks', 'Task') if apps.is_installed('tasks') else None
        # If the Task model isn't available yet, we still define the fields list.
        fields = ['id', 'project', 'title', 'description', 'status', 'priority', 'due_date', 'created_at']
        read_only_fields = ['id', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If Project becomes available later, ensure the field has a proper queryset.
        if Project and getattr(self.fields['project'], 'queryset', None) is None:
            self.fields['project'].queryset = Project.objects.all()

    def validate_due_date(self, value):
        if value and value < timezone.now().date():
            raise serializers.ValidationError("due_date cannot be in the past")
        return value

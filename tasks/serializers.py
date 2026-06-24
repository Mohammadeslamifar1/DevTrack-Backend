from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=None)

    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'description', 'status', 'priority', 'due_date', 'created_at']
        read_only_fields = ['id', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set queryset lazily to avoid circular import
        from projects.models import Project
        self.fields['project'].queryset = Project.objects.all()

    def validate(self, data):
        # Example: ensure due_date is not in the past
        due = data.get('due_date')
        if due and due < timezone.now().date():
            raise serializers.ValidationError("due_date cannot be in the past")
        return data

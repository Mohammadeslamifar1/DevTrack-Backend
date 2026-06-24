from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'owner', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']

from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description', 'owner__username')
    ordering = ('-created_at',)

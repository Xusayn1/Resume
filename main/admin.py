from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'github_link', 'demo_link')
    search_fields = ('title', 'description', 'technologies')
    list_filter = ('technologies',)

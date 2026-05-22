from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'topic',
        'supervisor',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'student__username',
        'topic__title',
    )

    autocomplete_fields = (
        'student',
        'topic',
        'supervisor',
    )

    ordering = (
        '-created_at',
    )

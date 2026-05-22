from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'supervisor',
        'is_available',
        'created_at',
    )

    list_filter = (
        'is_available',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    ordering = (
        'title',
    )

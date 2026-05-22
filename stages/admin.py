from django.contrib import admin
from .models import Stage


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
        'name',
        'status',
        'deadline',
        'order',
    )

    list_filter = (
        'status',
        'deadline',
    )

    search_fields = (
        'name',
        'project__student__username',
    )

    ordering = (
        'project',
        'order',
    )

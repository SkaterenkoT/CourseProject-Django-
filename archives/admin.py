from django.contrib import admin
from .models import Archive


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
        'archived_at',
    )

    list_filter = (
        'archived_at',
    )

    search_fields = (
        'project__student__username',
    )

    ordering = (
        '-archived_at',
    )

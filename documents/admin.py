from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
        'stage',
        'uploaded_by',
        'version',
        'uploaded_at',
    )

    list_filter = (
        'uploaded_at',
    )

    search_fields = (
        'project__student__username',
    )

    autocomplete_fields = (
        'project',
        'stage',
        'uploaded_by',
    )

    ordering = (
        '-uploaded_at',
    )

from django.contrib import admin
from .models import Defense


@admin.register(Defense)
class DefenseAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'project',
        'defense_date',
        'grade',
        'result',
    )

    list_filter = (
        'result',
        'defense_date',
    )

    search_fields = (
        'project__student__username',
    )

    filter_horizontal = (
        'commission',
    )

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'role',
        'study_group',
        'is_staff',
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'study_group',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Дополнительная информация',
            {
                'fields': (
                    'middle_name',
                    'role',
                    'study_group',
                    'phone_number',
                )
            },
        ),
    )

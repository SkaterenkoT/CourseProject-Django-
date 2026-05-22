from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        STUDENT = 'student', 'Студент'
        SUPERVISOR = 'supervisor', 'Руководитель'
        ADMIN = 'admin', 'Администратор'

    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )

    middle_name = models.CharField(
        max_length=150,
        blank=True
    )

    study_group = models.CharField(
        max_length=50,
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
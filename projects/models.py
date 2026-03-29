from django.db import models
from django.conf import settings


class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процессе'),
        ('on_review', 'На проверке'),
        ('defended', 'Защищено'),
        ('archived', 'В архиве'),
    ]

    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project'
    )

    topic = models.OneToOneField(
        'topics.Topic',
        on_delete=models.SET_NULL,
        null=True
    )

    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='supervised_projects'
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Project {self.id}"

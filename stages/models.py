from django.db import models
from projects.models import Project

class Stage(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_review', 'На проверке'),
        ('approved', 'Одобрено'),
        ('rejected', 'На доработке'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='stages'
    )

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    deadline = models.DateField()
    order = models.IntegerField()

    def __str__(self):
        return self.name

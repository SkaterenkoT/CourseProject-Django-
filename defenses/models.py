from django.db import models
from projects.models import Project

class Defense(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name='defense'
    )

    defense_date = models.DateTimeField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"Defense {self.project.id}"

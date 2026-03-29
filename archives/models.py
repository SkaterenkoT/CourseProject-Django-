from django.db import models

class Archive(models.Model):
    project = models.OneToOneField(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='archive'
    )

    archived_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Архив проекта {self.project.id}"

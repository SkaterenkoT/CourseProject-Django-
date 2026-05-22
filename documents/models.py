from django.db import models


class Document(models.Model):

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='documents'
    )

    stage = models.ForeignKey(
        'stages.Stage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='documents'
    )

    file = models.FileField(
        upload_to='documents/'
    )

    uploaded_by = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='uploaded_documents'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    version = models.PositiveIntegerField(
        default=1
    )

    description = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f"Документ #{self.id}"

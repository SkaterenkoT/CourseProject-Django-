from django.db import models


class Stage(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает'
        IN_REVIEW = 'in_review', 'На проверке'
        APPROVED = 'approved', 'Одобрено'
        REJECTED = 'rejected', 'На доработке'

    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='stages'
    )

    name = models.CharField(
        max_length=100
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    deadline = models.DateField()

    order = models.PositiveIntegerField()

    comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['order']
        unique_together = ('project', 'order')

        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'

    def __str__(self):
        return f"{self.project} - {self.name}"

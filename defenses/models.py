from django.db import models


class Defense(models.Model):

    class Result(models.TextChoices):
        PASSED = 'passed', 'Защищено'
        FAILED = 'failed', 'Не защищено'

    project = models.OneToOneField(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='defense'
    )

    defense_date = models.DateTimeField()

    grade = models.CharField(
        max_length=10
    )

    result = models.CharField(
        max_length=20,
        choices=Result.choices
    )

    commission = models.ManyToManyField(
        'users.User',
        related_name='commissions'
    )

    comment = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = 'Защита'
        verbose_name_plural = 'Защиты'

    def __str__(self):
        return f"Защита проекта {self.project.id}"

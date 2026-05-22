from django.db import models


class Project(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Черновик'
        ACTIVE = 'active', 'В процессе'
        REVIEW = 'review', 'На проверке'
        DEFENSE = 'defense', 'Допущен к защите'
        COMPLETED = 'completed', 'Завершён'
        ARCHIVED = 'archived', 'В архиве'

    student = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='project'
    )

    topic = models.ForeignKey(
        'topics.Topic',
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )

    supervisor = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='supervised_projects'
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f"Проект {self.student}"
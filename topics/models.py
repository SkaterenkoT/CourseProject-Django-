from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Тема диплома"
        verbose_name_plural = "Темы дипломов"

from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    supervisor = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='topics'
    )

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

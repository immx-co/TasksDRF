from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, blank=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

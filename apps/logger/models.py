# Django
from django.db import models


class Log(models.Model):
    created = models.DateTimeField()
    time = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    response = models.JSONField(blank=True)

    def __str__(self):
        return f'{self.path} {self.status}'

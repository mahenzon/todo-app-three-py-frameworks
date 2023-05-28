from django.db import models


class TodoItem(models.Model):
    text = models.CharField(max_length=50, null=False)
    done = models.BooleanField(null=False, default=False)

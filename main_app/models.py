from django.db import models
from datetime import datetime


class Feedback(models.Model):
    email = models.EmailField(max_length=50)
    comment = models.TextField(max_length=1000)
    created_on = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email

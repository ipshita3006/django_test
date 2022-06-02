from django.db import models
from django.db.models import Count


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(default=True)



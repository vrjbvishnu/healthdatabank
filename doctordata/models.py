from django.db import models
from __future__ import unicode_literals

# Create your models here.
class doctor(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    
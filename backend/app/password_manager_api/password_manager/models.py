from django.db import models
from django.contrib.postgres.fields import ArrayField

class LoginModel(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    user_name = models.CharField(max_length = 100, null=True, blank=True)
    password = models.CharField(max_length = 100, null=True, blank=True)
    #url = ArrayField(models.URLField(null=True, blank=True), blank=True)
    url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
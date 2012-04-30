from django.db import models

class Project(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=True)
    velocity = models.IntegerField(blank=False, null=False, default=8)
    iteration_term = models.IntegerField(blank=True, null=True, default=14)
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    update_at = models.DateTimeField(blank=False, auto_now_add=True)

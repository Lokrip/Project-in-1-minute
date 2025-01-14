from django.db import models
from django.contrib.auth.models import User

class UserSummary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_time = models.PositiveIntegerField(help_text="Time spent in minutes", null=True)
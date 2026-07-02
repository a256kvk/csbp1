from django.db import models

from django.contrib.auth.models import User

class PostModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

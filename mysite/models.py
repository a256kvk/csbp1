from django.db import models

from django.contrib.auth.models import User

class PostsModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class PrivateNotesModel(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    content = models.TextField()

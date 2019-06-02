from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    soundcloud = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
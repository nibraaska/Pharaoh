from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100, blank=True)
    image = models.FileField(upload_to='issues/{title}', blank=True, null=True)
    issue_link = models.CharField(max_length=100, blank=True)
    issue = models.FileField(upload_to='issues/{title}', blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True)
    soundcloud = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
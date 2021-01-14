from django.db import models
from django.conf import settings


class Note(models.Model):
    title = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Tag(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    tag = models.CharField(max_length=40)
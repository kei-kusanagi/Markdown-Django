from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    cheated_at = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.

class VideoContent(models.Model):
    link = models.URLField(blank=False, null=True, max_length=1000)
    video_description = models.CharField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_description
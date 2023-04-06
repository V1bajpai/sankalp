from django.db import models

# Create your models here.

class VideoContent(models.Model):
    link = models.URLField(blank=False, null=True, max_length=1000)
    video_description = models.CharField(blank=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_description

class TextContent(models.Model):
    category_choices = (
        ('Home','Home'),
        ('Latest','Latest'),
        ('Sports','Sports'),
        ('Election','Election'),
        ('Entertainment','Entertainment'),
        ('Technology','Technology'),
        ('Business','Business'),
        ('Education','Education'),
    )
    category = models.CharField(max_length=20, choices=category_choices, null=True, blank=True)
    title = models.TextField(blank=False)
    news = models.TextField(blank=False)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
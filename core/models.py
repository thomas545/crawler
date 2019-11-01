from django.db import models


class Youtube(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnail/photos/', blank=True, null=True)
    original_full_sized = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def create_video(self, title, video_url, duration, views, original_full_sized):
        youtube = Youtube()
        youtube.title = title
        youtube.video_url = video_url
        youtube.duration = duration
        youtube.views = views
        youtube.original_full_sized = original_full_sized
        youtube.save()
        return youtube


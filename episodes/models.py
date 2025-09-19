from django.db import models


class Episode(models.Model):
    episode_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"Episode {self.episode_number}: {self.title}"

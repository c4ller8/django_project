from django.db import models
from cloudinary.models import CloudinaryField


class Episode(models.Model):
    episode_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"Episode {self.episode_number}: {self.title}"

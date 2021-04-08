from django.db import models
from django.urls import reverse

# Create your models here.

# Artist Model
class Artist(models.Model):

    # Artist model fields
    name = models.CharField(max_length=120)
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.pk})

    # String Magic Method
    # Makes debugging easier!
    def __str__(self):
        return self.name

# Album model
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    year = models.IntegerField()
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

# Artist Model
class Artist(models.Model):

    # Artist model fields
    name = models.CharField(max_length=120)
    bio = models.TextField()

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

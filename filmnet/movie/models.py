from django.db import models


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    summary = models.TextField()
    rate = models.CharField(max_length=100)
    duration = models.CharField(max_length=150)
    genres = models.CharField(max_length=100)
    actors = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'movie'

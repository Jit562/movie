from django.db import models

# Create your models here.

class MovieModel(models.Model):
    title = models.CharField(max_length=120)
    vote_average = models.CharField(max_length=20)
    vote_count = models.CharField(max_length=20)
    release_date = models.DateField()
    overview = models.TextField()
    popularity = models.CharField(max_length=30)
    poster_path = models.ImageField(upload_to="movie")

    def __str__(self):
        return self.title

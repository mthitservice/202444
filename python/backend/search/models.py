from django.db import models

# models.py
class Movie(models.Model):
    title=models.CharField(max_length=255)
    director=models.CharField(max_length=255)
    plot=models.TextField()
    year=models.IntegerField()

    def __str__(self):
        return self.name
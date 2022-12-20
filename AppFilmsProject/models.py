from django.db import models


class Category(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Film(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_date = models.DateField()
    actors = models.TextField()
    show_date = models.DateField()

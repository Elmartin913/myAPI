from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, null=True)
    task = models.CharField(max_length=128, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Person, related_name='actors')
    year = models.ImageField(null=True)
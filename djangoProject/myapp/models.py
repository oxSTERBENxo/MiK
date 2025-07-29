from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    background = models.ImageField(upload_to="background_photos/", null=True, blank=True)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Polaroid(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="polaroid_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.country.name}"

class Question(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.country.name} {self.content}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.question} {self.content}"
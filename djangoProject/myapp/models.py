from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length=100)
    background = models.ImageField(upload_to="background_photos/", null=True, blank=True)
    color = models.CharField(max_length=100)
    flag_emoji = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Polaroid(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="polaroid_photos/", null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)

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
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} {self.content}"


class Song(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return f"{self.country.name} song"
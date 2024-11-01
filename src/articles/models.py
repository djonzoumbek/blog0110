from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField('Category')
    tags = models.CharField(max_length=50)
    nb_likes = models.IntegerField(default=0, null=True, blank=True)
    nb_dislikes = models.IntegerField(default=0, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    published_date = models.DateField(auto_now_add=False, null=True, blank=True)
    image = models.ImageField(upload_to="articles/", null=True, blank=True)

    def __str__(self):
        return self.title

    def add_like(self):
        self.nb_likes += 1
        self.save()
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField('slug', max_length=100, unique=True, default="none")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()
    body = models.TextField()
    media = models.URLField()
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

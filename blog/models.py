from django.db import models
from django.core import validators


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(
        validators=[
            validators.MinLengthValidator(20),
        ],
    )


class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name="tags")

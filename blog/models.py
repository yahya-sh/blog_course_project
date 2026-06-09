from django.db import models
from django.core import validators
from django.urls import reverse
from django.templatetags.static import static


class PostManager(models.Manager):
    def latest_posts(self):
        return self.order_by("-date")[:3]


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
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
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def get_absolute_url(self) -> str:
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def get_cover_image_url(self) -> str:
        return static(f"blog/posts_covers/{self.cover_image}")

    objects = PostManager()

    def __str__(self):
        return self.title

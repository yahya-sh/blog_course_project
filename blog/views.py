from django.shortcuts import render
from . import models
from django.views.generic import DetailView


# Create your views here.
def index(request):
    latest_posts = models.Post.objects.latest_posts()
    return render(
        request,
        "blog/index.html",
        {
            "latest_posts": latest_posts,
        },
    )


class PostDetail(DetailView):
    model = models.Post
    slug_field = "slug"
    template_name = "blog/detail.html"

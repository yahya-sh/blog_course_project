from django.shortcuts import render
from . import models


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

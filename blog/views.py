from django.shortcuts import render
from . import models
from django.views.generic import DetailView, ListView


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


class PostsList(ListView):
    model = models.Post
    template_name = "blog/all.html"
    context_object_name = "all_posts"

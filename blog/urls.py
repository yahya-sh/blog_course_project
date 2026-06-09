from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("all-posts/", views.PostsList.as_view(), name="all"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="detail"),
]

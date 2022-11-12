from django.urls import path
from . import views

app_name = "all_videos"

urlpatterns = [
    path("videos", views.all_videos, name="all_videos"),
    path("category/<slug:slug>", views.category_detail, name="cat_det"),
    path("detail/<slug:slug>", views.video_detail, name="detail"),
    path("search/", views.search_videos, name="search")
]
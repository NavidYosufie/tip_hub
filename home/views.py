from django.shortcuts import render, get_object_or_404
from videos.models import Video, Category_Detail, Category

def show_video(request):
    videos = Video.objects.all().order_by("-created",)[:6]
    return render(request, "index.html", context={"videos": videos})








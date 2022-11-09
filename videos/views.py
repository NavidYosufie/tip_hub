from django.shortcuts import render, get_object_or_404
from .models import Video, Category_Detail
from django.core.paginator import Paginator

def all_videos(request):
    video = Video.objects.all()
    get_page_number = request.GET.get("page")
    paginator = Paginator(video, 2)
    object_list = paginator.get_page(get_page_number)
    return render(request, "all-videos.html", {"videos": object_list})


def video_detail(request, slug):
    videos_detail = get_object_or_404(Video, slug=slug)
    return render(request, "video-detail.html", {"videos": videos_detail})


def category_detail(request, slug):
    cat_det = get_object_or_404(Category_Detail, slug=slug)
    videos = cat_det.video_set.all()
    return render(request, "all-videos.html", {"videos": videos})
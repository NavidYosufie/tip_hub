from django.shortcuts import render, get_object_or_404
from .models import Video, Category_Detail, Comment
from django.core.paginator import Paginator

def all_videos(request):
    video = Video.objects.all()
    get_page_number = request.GET.get("page")
    paginator = Paginator(video, 2)
    object_list = paginator.get_page(get_page_number)
    return render(request, "all-videos.html", {"videos": object_list})


def video_detail(request, slug):
    videos_detail = get_object_or_404(Video, slug=slug)
    if request.method == 'POST':
        body = request.POST.get("body")
        parent_id = request.POST.get("parent_id")
        Comment.objects.create(body=body, videos=videos_detail, user=request.user, parent_id=parent_id)
    return render(request, "video-detail.html", {"videos": videos_detail})


def category_detail(request, slug):
    cat_det = get_object_or_404(Category_Detail, slug=slug)
    videos = cat_det.video_set.all()
    return render(request, "all-videos.html", {"videos": videos})

def search_videos(request):
    search = request.GET.get("search")
    videos = Video.objects.filter(title__icontains=search)
    get_number_page = request.GET.get("page")
    paginator = Paginator(videos, 1)
    object_list = paginator.get_page(get_number_page)
    return render(request, "all-videos.html", {"videos": object_list})
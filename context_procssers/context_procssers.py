from videos.models import Category, Category_Detail



def categourie(request):
    categouries = Category_Detail.objects.order_by("-created",)
    return {"categouries": categouries}

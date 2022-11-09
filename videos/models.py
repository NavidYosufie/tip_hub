from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Category_Detail(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("all_videos:cat_det", kwargs={"slug": self.slug})

    #def save(self):
     #   self.slug = slugify(self.title)
      #  super(Category_Detail, self).save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(blank=True, null=True, max_length=200)
    category = models.ManyToManyField(Category_Detail, null=True, blank=True)
    created = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title


class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to="Videos", blank=True, null=True)
    image = models.ImageField(upload_to="Videos/image", blank=True, null=True)
    time_videos = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category_Detail, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.title}  -  {self.author}"

    def get_absolut_url(self):
        return reverse("all_videos:detail", kwargs={"slug": self.slug})

    #def save(self):
     #   self.slug = slugify(self.title)
     #   super(Video, self).save()


class Comment(models.Model):
    videos = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.body[:30]







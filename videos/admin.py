from django.contrib import admin
from .models import Category_Detail, Video, Category, Comment

admin.site.register(Category_Detail)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Comment)
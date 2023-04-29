from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from tagify.fields import TagField

from .forms import PostForm
from .models import Post, Tag

# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10
@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display=('title', 'created_at', 'my_tags')
    search_fields=('title', 'content')
    list_filter=('created_at',)
    form=PostForm
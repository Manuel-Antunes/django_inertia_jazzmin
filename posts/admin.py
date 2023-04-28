from django.contrib import admin
from .models import Post
from django import forms
# Register your models here.
class BaseAdmin(admin.ModelAdmin):
  list_per_page = 10
  
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
  
@admin.register(Post)
class PostAdmin(BaseAdmin):
  list_display = ('title', 'created_at')
  search_fields = ('title', 'content')
  list_filter = ('created_at',)
  form = PostForm

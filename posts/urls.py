from django.urls import path

from .views import chat

app_name = 'posts'

urlpatterns = [
  path('<int:id>/post/chat', chat, name='chat'),
]
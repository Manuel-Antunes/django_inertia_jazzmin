from django.urls import path
from .views import chat

app_name = 'posts'

urlpatterns = [
  path('<int:id>/chat', chat, name='chat'),
]
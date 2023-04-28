from django.contrib.auth.decorators import login_required
from inertia import render
from .models import Post
from django.contrib.admin.sites import site
# Create your views here.

@login_required
def chat(request,id):
  ctx = site.each_context(request)
  post = Post.objects.get(id=id)
  return render(request, "Post/Chat", template_data=ctx, props={
    'post': post
  })
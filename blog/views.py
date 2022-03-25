from django.shortcuts import render

from .models import Post


# Create your views here.
def posts(request):
    post = Post.objects.first()
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts, 'post': post})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog.html', {'post': post})

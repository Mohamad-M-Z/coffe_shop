from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {"posts": posts}
    return render(request, 'coffe_shop/blog.html', context)
from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs['cat_name'])

    context = {"posts": posts}
    return render(request, 'coffe_shop/blog.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts" : posts}
    return render(request,'coffe_shop/blog-home.html',context)
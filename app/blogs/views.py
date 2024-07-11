from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        blog_image = request.FILES.get('blog_image')
        blog_name = data.get('blog_name')
        blog_description = data.get('blog_description')
        author = data.get('author')
        Blog.objects.create(
            blog_image=blog_image,
            blog_name=blog_name,
            blog_description= blog_description,
            author= author)
        return redirect('home')

    queryset = Blog.objects.all()
    context = {
        'home': queryset
    }
    return render(request, "home.html",context)

def publish(request):
    if request.method == "POST":
        data = request.POST
        blog_image = request.FILES.get('blog_image')
        blog_name = data.get('blog_name')
        blog_description = data.get('blog_description')
        author = data.get('author')
        Blog.objects.create(
            blog_image=blog_image,
            blog_name=blog_name,
            blog_description=blog_description,
            author=author)
        return redirect('publish')

    queryset = Blog.objects.all()
    context = {
        'home': queryset
    }
    return render(request, "publish.html",context)

def update_blog(request, id):
    queryset = Blog.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        blog_image = request.FILES.get('blog_image')
        blog_name = data.get('blog_name')
        blog_description = data.get('blog_description')
        author = data.get('author')

        queryset.blog_name = blog_name
        queryset.blog_description = blog_description
        queryset.author = author

        if blog_image:
            queryset.blog_image = blog_image

        queryset.save()
        return redirect('publish')

    context ={'blog': queryset}
    return render(request, "update_blog.html", context)
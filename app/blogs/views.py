from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
def login_page(request):


    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")

        user = authenticate(request, username = username, password = password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("/publish/")

    return render(request, "login.html")
def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect("/register/")

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully")

        return redirect('/register/')
    return render(request,"register.html")
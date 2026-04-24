from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Blog


# Create your views here.
def mainpage(request):

    return render(request, 'main/mainpage.html')

def blogpage(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogpage.html', {'blogs': blogs})

def new_blog(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    return render(request, 'main/new_blog.html')

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    new_blog = Blog()

    new_blog.title = request.POST['title']
    new_blog.writer = request.user.username
    new_blog.pub_date = request.POST['pub_date']
    new_blog.content = request.POST['content']

    new_blog.save()

    return redirect('main:detail', new_blog.id)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/detail.html', {'blog': blog})

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if edit_blog.writer != request.user.username:
        return redirect('main:detail', edit_blog.id)

    return render(request, 'main/edit.html', {"blog": edit_blog})

def update(request, blog_id):
    update_blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if update_blog.writer != request.user.username:
        return redirect('main:detail', update_blog.id)

    update_blog.title = request.POST['title']
    update_blog.writer = request.user.username
    update_blog.pub_date = request.POST['pub_date']
    update_blog.content = request.POST['content']
    update_blog.save()

    return redirect('main:detail', update_blog.id)

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if delete_blog.writer != request.user.username:
        return redirect('main:detail', delete_blog.id)

    delete_blog.delete()

    return redirect('main:blogpage')

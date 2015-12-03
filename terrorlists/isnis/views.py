from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'isnis/main.html', {'posts': posts})

def login(request):
    return render(request, 'isnis/login.html',{})

def register(request):
    return render(request, 'isnis/register.html',{})

@login_required
def post_remove(request, post_id, post_author):
    post = get_object_or_404(Post, pk=post_id)
    if str(post.author) is post_author or str(post.author) == post_author:
        post.delete()
    return redirect('isnis.views.main')

@login_required
def new(request):
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        if a == '' or b == '' or c == '':
            return redirect('isnis.views.main')
        form = PostForm({'title':a, 'position':b, 'text':c})
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('isnis.views.main')
    else:
        return redirect('isnis.views.main')

@login_required
def edit(request, post_author, pk):
    post = get_object_or_404(Post, pk=pk)
    if str(post.author) is post_author or str(post.author) == post_author:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'isnis/main.html', {'posts': posts, 'id':pk})
    else :
        return redirect('isnis.views.main')

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        form = PostForm({'title':a, 'position':b, 'text':c}, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('isnis.views.main')
    else:
        form = PostForm(instance=post)
    return redirect('isnis.views.main')

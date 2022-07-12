from multiprocessing import context
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from post.forms import PostCreationForm

from post.models import Post


def home_page(request):
    posts = Post.objects.all()      
    context = {'all_posts' : posts, }
    return render (request , 'post/pages/home_page.html', context)

def post_view(request, username, post_id):
    user = User.objects.get(username=username)
    post = get_object_or_404(Post, pk=post_id, author=user )
    likes = post.likes.all()
    myself = User.objects.get(id=request.user.id)
    liked = myself in likes 
    context = {'post' : post,'likes' : likes, 'liked' : liked,  }

    return render (request , 'post/pages/post_view.html', context)

def post_create(request):
    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm (request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            post.author = user
            post.save()
            return redirect('account:user_dashbord')
    context = {'post_form' : form}
    return render (request , 'post/pages/post_create.html', context)

def post_like(request, post_id, username):
    user = User.objects.get(username=username)
    post = get_object_or_404(Post, pk=post_id, author=user)
    likes = post.likes.all()
    myself = User.objects.get(id=request.user.id)
    liked = myself in likes 
    if not liked:
        post.likes.add(myself)
    return redirect('post:post_view', username=username, post_id=post_id)

def post_unlike(request, post_id, username):
    user = User.objects.get(username=username)
    post = get_object_or_404(Post, pk=post_id, author=user)
    likes = post.likes.all()
    myself = User.objects.get(id=request.user.id)
    liked = myself in likes 
    if liked:
        post.likes.remove(myself)
    return redirect('post:post_view', username=username, post_id=post_id)
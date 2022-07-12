from ast import If
from re import U
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from accounts.utils import make_pair
from accounts.forms import UserRrgisterForm, UserLoginForm,EditDashboardForm
from accounts.models import UserProfile, UserRelation
from post.models import Post


def index(request):
    return render(request, "pages/index.html")

def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in your account." , "success")
                return redirect("account:user_dashbord")
            else:
                messages.error(request, "There is no account with this username.")
    context = {'login_form': form}
    return render(request, "pages/signin.html", context)

def register(request):
    form = UserRrgisterForm()
    if request.method == "POST":
        form = UserRrgisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = make_password(form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            messages.success(request, "Account created successfully." , "success")
            return redirect("account:user_login")

    context = {'register_form': form}
    return render(request, "pages/register.html", context)

@login_required
def user_logout(request):
    logout(request)
    return redirect("account:user_login")

@login_required
def user_dashbord(request):
    profile = UserProfile.objects.get(user=request.user.id)
    posts = User.objects.get(id=request.user.id).posts.all()
    user = User.objects.get(id=request.user.id)
    post_length = len(posts)
    posts = make_pair(list(posts))
    context = {'user_profile':profile , 'user_posts' : posts, 'post_length' : post_length, 'user': user }

    return render(request, "pages/dashboard.html", context)


@login_required
def user_profile(request, username):
    if request.user.username == username:
        return redirect('account:user_dashbord')

    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user.id)
    posts = User.objects.get(id=user.id).posts.all()
    post_length = len(posts)
    posts = make_pair(list(posts))
    rel = UserRelation.objects.filter(follower=request.user, following=user).exists()
    context = {'user_profile':profile , 'user':user , 'user_posts' : posts, 'post_length' : post_length, 'rel':rel}

    return render(request, "pages/profile.html", context)
 

@login_required
def edit_dashboard(request):
    profile = UserProfile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form=EditDashboardForm(request.POST)
        user = User.objects.get(id=request.user.id)
        user.first_name=form['first_name'].value()
        user.last_name=form['last_name'].value()
        user.save()
        form = EditDashboardForm(request.POST, request.FILES, instance=profile)
        form.save()

        return redirect('account:user_dashbord')
    edit_dashboard_form = EditDashboardForm(initial={
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'about': profile.about,

    })
    context = {'form': edit_dashboard_form}

    return render(request, "pages/edit_dashboard.html", context)
 
@login_required
def user_following(request, username):
    if request.user.username == username :
        return redirect('account:user_dashbord')
    user_target = get_object_or_404(User, username=username)
    rel = UserRelation.objects.filter(follower=request.user, following=user_target)
    if not rel: 
        UserRelation.objects.create(follower=request.user, following=user_target)
    return redirect('account:user_profile', username=username)

@login_required
def user_unfollowing(request, username):
    if request.user.username == username :
        return redirect('account:user_dashbord')
    user_target = get_object_or_404(User, username=username)

    rel = UserRelation.objects.filter(follower=request.user, following=user_target).exists()
    if rel: 
        UserRelation.objects.get(follower=request.user, following=user_target).delete()
    return redirect('account:user_profile', username=username)
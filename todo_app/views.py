from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login as auth_login, logout
from base_user.forms import MyUserCreationForm
from .forms import *
from .models import *


# Create your views here.
def add(request):
    context = {}
    context['form'] = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
    return render(request, 'index.html', context)


def update(request, id):
    context = {}
    post = Post.objects.filter(id=id).last()
    context['post'] = post
    context['form'] = UpdateForm(instance=post)
    if request.method == 'POST':

        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            UpdatedPosts.objects.create(
                post=post,
                text=post.text,
                desc=post.desc,
                version=post.version
            )
            post.version += 1

            form.save()
        return redirect('/')

    return render(request, 'update.html', context)


def register(request):
    context = {}

    form = MyUserCreationForm()
    context['form'] = form
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print('VASLIDDDD')
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/')
        else:
            pass

    return render(request, 'register.html', context)


def login(request):
    context = {}
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                auth_login(request, user)
                return redirect('/')
            else:
                pass

    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")


def myfiles(request, id):
    context = {}
    context['files'] = Post.objects.filter(user_id=id)
    return render(request, 'files.html', context)

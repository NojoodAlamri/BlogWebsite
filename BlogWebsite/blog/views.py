from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Category, Post, Comment


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def users(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def blogs(request):
    blog = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'blog': blog
    }
    return HttpResponse(template.render(context, request))


def comments(request):
    comment= Comment.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
        'comment': comment
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    category = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))


def blogdetails(request, id):
    blog = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'blog': blog
    }
    return HttpResponse(template.render(context, request))
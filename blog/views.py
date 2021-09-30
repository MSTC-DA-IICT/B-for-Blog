from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def create_blog(request):
    return render(request, 'create_blog.html')

def read_blog(request):
    return render(request, 'read_blog.html')
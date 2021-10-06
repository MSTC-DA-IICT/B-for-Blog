"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from blog.views import index, login, create_blog, read_blog, registration

urlpatterns = [
    path('', index, name="index"),
    path('index', index, name="index"),
    path('login', login, name='login'),
    path('create_blog', create_blog, name='create_blog'),
    path('read_blog', read_blog, name='read_blog'),
    path('registration', registration, name='registration'),
]
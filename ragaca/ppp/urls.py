from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('create_articles/', views.create_articles, name='create_articles'),
]

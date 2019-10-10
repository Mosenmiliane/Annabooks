from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('home/', views.index, name='index_url'),
    path('home/articles/', views.all_articles, name='all_articles_url'),
    re_path('(?P<id>[0-9]+)/', views.one_article, name='one_article_url'),
    path('search/', views.search, name='search_url'),

]
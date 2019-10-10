from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.all_books, name='all_books_url'),
    re_path('(?P<id>[0-9]+)/', views.one_book, name='one_book_url'),


    ]
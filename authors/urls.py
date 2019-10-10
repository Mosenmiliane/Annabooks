from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.all_authors, name='all_authors_url'),
    re_path('(?P<id>[0-9]+)/', views.one_author, name='one_author_url'),

]
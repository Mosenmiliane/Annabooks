from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from books.models import Article, Author, Book, Review
from itertools import chain

def index(request):
    article = Article.objects.all()
    return render(request, 'home/index.html', {'articles': article})

def all_articles(request):
    article = Article.objects.filter(visible=True)
    return render(request, 'home/all_articles.html', {'articles': article})

def one_article(request, id):
     article = Article.objects.get(id=id)
     return render(request, 'home/one_article.html', {'article': article})

def search(request):
    query = request.GET.get('q')

    books = Book.objects.filter(Q(title__contains=query) | Q(original_title__contains=query))
    authors = Author.objects.filter(Q(name_rus__contains=query) | Q(name__contains=query) | Q(second_name__contains=query))
    reviews = Review.objects.filter(title__contains=query)

    search_results = chain(books, authors, reviews)
    return render(request, 'home/search_results.html', {'search_results': search_results})




from django.shortcuts import render
from books.models import Author
from books.models import Book

def all_authors(request):
    authors = Author.objects.order_by('name_rus')
    all_authors_books = {}
    for a in authors:

        print('!!!!!!!', a.name)
        current_author_books = Book.objects.filter(author=a)
        print('---------', 'current author name is ', a.name, 'and current author books are: ', current_author_books)
        all_authors_books[a.id] = current_author_books

    print('**************************', 'ALL BOOKS FOR ALL AUTHORS', all_authors_books)
    return render(request, 'authors/all_authors.html', {'authors': authors, 'all_authors_books': all_authors_books})

def one_author(request, id):
    author = Author.objects.get(id=id)
    books_author = Book.objects.filter(author=author)
    number = len(books_author)
    return render(request, 'authors/one_author.html', {'author': author, 'books_author': books_author, 'number': number})

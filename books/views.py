from django.shortcuts import render
from books.models import Book
from books.models import Author
from books.forms import ReviewForm
from datetime import datetime
from django.http import HttpResponse
from books.models import Review
from django.contrib.auth import authenticate, login
from books.forms import LoginForm




def all_books(request):
    books = Book.objects.filter(visible=True)
    return render(request, 'books/all_books.html', {'books': books})

def one_book(request, id):
    book = Book.objects.get(id=id)
    reviews = Review.objects.filter(book=book, visible=True)
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        user = request.user
        print('USER !!!!!!!', user)
        if not request.user.is_authenticated:
            return HttpResponse('Пожалуйста, авторизируйтесь, чтобы оставить комментарий')

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            new_form = form.save(commit = False)
            book = Book.objects.get(id=id)
            new_form.user = request.user
            new_form.book = book

            print('**********', datetime.now(), book)
            new_form.save()

            return HttpResponse('Ваша рецензия была отправлена на модерацию и будет в скором времени опубликована. Спасибо!')
    else:
        form = ReviewForm()
    return render(request, 'books/one_book.html', {'book': book, 'form': form, 'reviews': reviews})

def user_login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('OK')
                    else:
                        return HttpResponse('Пользователь не найден')
                else:
                    return HttpResponse('Логин не действителен')
            else:
                form = LoginForm()
            return render(request, 'books/login.html', {'form': form})



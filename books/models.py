from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import admin
import datetime
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from tinymce.models import HTMLField

User = get_user_model()

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="100" style="object-fit: cover;"/></a> %s ' % \
                          (image_url, image_url, file_name, ('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class Author(models.Model):
    name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    name_rus = models.CharField(max_length=200, default="Name in Russian")
    books = models.CharField(max_length=200000)
    photo = models.FileField(upload_to='author_img/', blank=True)
    biography = HTMLField(default="Author's biography")

    def __str__(self):
        return str(self.name+' '+self.second_name)

    class Meta:
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'

class Book(models.Model):
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200, default="Original_title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    anna_review = HTMLField(default="Anna's review")
    image = models.FileField(upload_to='book_img/', blank=True)
    visible = models.BooleanField(default=True)

    @mark_safe
    def small_image(self):
        return f'<img src="{self.image.url}" width="200">' if self.image else ''
    small_image.short_description = 'Logo'
    small_image.allow_tags = True


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default="Ваш отзыв")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    visible = models.BooleanField(default=False)

class Article(models.Model):
    title = models.CharField(max_length=2000)
    text = models.TextField(default="Текст статьи")
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.FileField(upload_to='article_img/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
       return str(self.title)

    class Meta:
       verbose_name_plural = 'Articles'
       verbose_name = 'Article'


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_title', 'author', 'small_image')
    list_filter = ('author', 'rating')
    fields = ('title', 'original_title', 'author', 'year', 'rating', 'anna_review', 'image', 'visible')
    list_display_links = ('title', 'author')
#    readonly_fields = ('small_image',)

class BookInLine(admin.TabularInline):
    model = Book
    formfield_overrides = {models.FileField: {'widget': AdminImageWidget}}
    fields = ('title', 'year', 'image')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'name_rus')
    list_filter =('name', 'second_name', 'name_rus')
    fields = ('name', 'second_name', 'name_rus', 'photo', 'biography')
    list_display_links = ('name', 'second_name', 'name_rus')
    inlines = [
        BookInLine]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'book')
    list_filter = ('user', 'book')
    fields = ('title', 'book', 'text', 'visible', 'user',)
    list_display_links = ('title', 'book')
    readonly_fields = ('user',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    fields = ('title', 'text', 'user', 'visible', 'image')
    list_display_links = ('title', 'text')




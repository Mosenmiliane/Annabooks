from django.contrib import admin

from .models import Author, Book, Review, Article, AuthorAdmin, BookAdmin, ReviewAdmin, ArticleAdmin

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Article, ArticleAdmin)


admin.site.site_header = "Anna's book ADMIN"

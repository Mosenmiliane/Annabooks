from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('authors/', include('authors.urls')),
    path('', include('home.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

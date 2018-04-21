from django.urls import path

from . import views


urlpatterns = [
    path('authors/', views.authors_list),
    path('authors/<int:author_id>', views.authors_detail, 
        name='author_detail'),
    path('books/', views.books_list),
    path('books/<int:book_id>', views.books_detail, 
        name='book_detail'),
]

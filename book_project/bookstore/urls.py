from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.books_list, name="book_list"),
    path('books/<int:book_id>', views.books_details, name="book_details"),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('authors/', views.authors_list, name="author_list"),
    path('authors/<int:author_id>/', views.authors_details, name="author_details"),
    path('add_book/<int:author_id>/', views.add_book, name="add_book"),
    path('edit_book/<int:book_id>/', views.edit_book, name = "edit_book"),
    path('book_edit/<int:book_id>/', views.book_edit, name = "book_edit"),
]
from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect
from bookstore.models import Book, Author

from django.shortcuts import get_object_or_404, render
def index(request):
  return render(request, 'index.html')


def books_list(request):
  books = Book.objects.all().order_by('-created_at')
  return render(request, 'book/book_list.html', {"book_list": books, "active_menu": "book"})


def books_details(request, book_id):
  book = Book.objects.get(pk=book_id)
  return render(request, 'book/book_details.html', {"book": book, "active_menu": "book"})


def authors_list(request):
  authors = Author.objects.all()
  return render(request, 'author/author_list.html', {"author_list": authors, "active_menu": "author"})


def authors_details(request, author_id):
  author = Author.objects.get(pk=author_id)
  books = author.book_set.all();

  return render(request, 'author/authors_details.html', 
    {"author": author, "active_menu": "author", "books": books})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()

    return HttpResponseRedirect(reverse('books:index', args=()))

def add_book(request, author_id):
    a = Author.objects.get(pk = author_id)
    data = request.POST
    b = Book()
    b.title = data.get("title", "")
    b.author = a
    b.save()

    return HttpResponseRedirect(reverse('books:book_list'))

def edit_book(request, book_id):
    b = Book.objects.get(pk = book_id)
    data = request.POST
    b.title = data.get('title', b.title)
    b.save()
    return HttpResponseRedirect(reverse('books:book_list'))

def book_edit(request, book_id):
     b = Book.objects.get(pk = book_id)
     return render(request, "book/book_edit.html", {"book" : b})


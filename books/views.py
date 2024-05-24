from django.shortcuts import render
from .models import Book

# Create your views here.
def books(request):
    return render(request, 'books/books.html', {'books': Book.objects.all()})

def book(request):
    return render(request, 'books/book.html')

def borrowed(request):
    books = Book.objects.all()
    x = {'books' : books.filter(borrowed=True)}
    return render(request, 'books/borrowed.html', x)
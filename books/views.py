from django.shortcuts import render
from .models import Book, User

# Create your views here.
def signup(request):
    if(request.method == 'POST'):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = User(
                fullname= fullname, 
                email = email, 
                username= username, 
                password= password
            )
        data.save()
    
    return render(request, 'books/signup.html')

def books(request):
    return render(request, 'books/books.html', {'books': Book.objects.all()})

def book(request):
    return render(request, 'books/book.html')

def borrowed(request):
    books = Book.objects.all()
    x = {'books' : books.filter(borrowed=True)}
    return render(request, 'books/borrowed.html', x)
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from .models import Book, User

# Create your views here.

def signup_page(request):
    return render(request, 'books/signup.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        errors = {}
        if not username:
            errors['username'] = 'Username is required.'
        if not password:
            errors['password'] = 'Password is required.'
            
        if errors:
            return JsonResponse({'success': False, 'errors': errors})
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Log the user in
            auth_login(request, user)
            return redirect('books')  # Redirect to the books page
        else:
            errors['auth'] = 'Invalid username or password.'
            return JsonResponse({'success': False, 'errors': errors})
    
    return render(request, 'books/login.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the input fields
        errors = {}
        if not fullname:
            errors['fullname'] = 'Fullname is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not username:
            errors['username'] = 'Username is required.'
        if not password:
            errors['password'] = 'Password is required.'
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors})

        # Saving
        user = User(
            fullname=fullname,
            email=email,
            username=username,
            password=password
        )
        user.save()

        return JsonResponse({'success': True, 'message': 'User registered successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

def books(request):
    return render(request, 'books/books.html', {'books': Book.objects.all()})

def book(request):
    return render(request, 'books/book.html')

def borrowed(request):
    books = Book.objects.all()
    x = {'books' : books.filter(borrowed=True)}
    return render(request, 'books/borrowed.html', x)
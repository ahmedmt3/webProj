from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from .models import Book, User

# Create your views here.

def books(request):
    return render(request, 'books/books.html', {'books': Book.objects.all()})

def user_books(request):
    username = request.session.get('username', 'Guest')
    fullname = get_object_or_404(User, pk=username)
    return render(request, 'books/userBooks.html', {'books': Book.objects.all(), 'fullname' : fullname, 'username' : username})

def book(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'books/book.html', {'book': book})

def user_book(request, id, username):
    book = get_object_or_404(Book, pk=id)
    fullname = get_object_or_404(User, pk=username)
    return render(request, 'books/userBook.html', {'book': book, 'fullname' : fullname, 'username' : username})

def borrowed(request):
    books = Book.objects.all()
    x = {'books' : books.filter(borrowed=True)}
    return render(request, 'books/borrowed.html', x)

def signup_page(request):
    return render(request, 'books/signup.html')

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
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            errors['username'] = 'Username already taken.'
            return JsonResponse({'success': False, 'errors': errors})
        if User.objects.filter(email=email).exists():
            errors['email'] = 'Email address already taken.'
            return JsonResponse({'success': False, 'errors': errors})
        
        # Saving
        user = User(
            fullname=fullname,
            email=email,
            username=username,
            password=password
        )
        user.save()

        return JsonResponse({'success': True, 'message': 'User registered successfully.', 'redirect': '/login/'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def login_page(request):
    return render(request, 'books/login.html')

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         errors = {}
#         if not username:
#             errors['username'] = 'Username is required.'
#         if not password:
#             errors['password'] = 'Password is required.'
            
#         if errors:
#             return JsonResponse({'success': False, 'errors': errors})
        
#         # Check if the username exists in the database
#         try:
#             user = User.objects.get(username=username, password=password)
#             return JsonResponse({'success': True, 'message': 'Login successful.', 'redirect': '/application/books/', 'username' : username})
        
#         except User.DoesNotExist:
#             errors['password'] = 'Invalid username or password.'
#             return JsonResponse({'success': False, 'errors': errors})
        
#     JsonResponse({'success': False, 'errors': 'Invalid Request Method'})
        
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
        
        # Check if the username exists in the database
        try:
            user = User.objects.get(username=username, password=password)
            # Store username in session
            request.session['username'] = username
            return JsonResponse({'success': True, 'message': 'Login successful.', 'redirect': '/application/books/'})
        
        except User.DoesNotExist:
            errors['password'] = 'Invalid username or password.'
            return JsonResponse({'success': False, 'errors': errors})
        
    return JsonResponse({'success': False, 'errors': 'Invalid Request Method'})
    

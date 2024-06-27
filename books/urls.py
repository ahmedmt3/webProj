from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('', views.books, name='books'),
    # path('book', views.book, name='book'),
    path('books/borrowed', views.borrowed, name='borrowed'),
    path('signup/', views.signup_page, name='signup_page'),
    path('signup/submit/', views.signup, name='signup'), #signup func. url
    path('login/', views.login_page, name='login_page'),
    path('login/submit/', views.login, name='login'), #login func. url
    path('books/<int:id>/', views.book, name='book_details'),

    path('application/books/', views.user_books, name='user_books'),
    path('application/books/<str:username>/<int:id>/', views.user_book, name='user_book'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('book', views.book, name='book'),
    path('borrowed', views.borrowed, name='borrowed'),
    path('signup', views.signup, name='signup'),
]
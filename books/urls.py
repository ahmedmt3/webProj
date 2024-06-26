from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    # path('book', views.book, name='book'),
    path('borrowed', views.borrowed, name='borrowed'),
    path('signup/', views.signup_page, name='signup_page'),
    path('signup/submit/', views.signup, name='signup'), #signup func. url
    path('login/', views.login, name='login'),
    path('/<int:id>', views.book, name='book_details'),
]
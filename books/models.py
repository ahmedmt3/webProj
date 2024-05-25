from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50, default='Full name')
    email = models.CharField(max_length=50, default='email@email.com')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
    
class Book(models.Model):
    categ = [
        ('Classic', 'Classic'),
        ('Ciction', 'Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Biography', 'Biography'),
        ('Science Fiction', 'Science Fiction'),
        ('Historical Fiction', 'Historical Fiction'),
    ]
    
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices= categ)
    image = models.ImageField(upload_to= 'uploadedPhotos/%y/%m/%d')
    borrowed = models.BooleanField(default= False)
    
    def __str__(self):
        return self.title
    
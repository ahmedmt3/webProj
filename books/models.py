from django.db import models

# Create your models here.

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
    
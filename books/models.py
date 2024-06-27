from django.db import models

# Create your models here.

class User(models.Model):
    
    fullname = models.CharField(max_length=50, default='Full name')
    email = models.CharField(max_length=50, default='email@email.com')
    username = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50)
    # borrowed_books = models.ManyToManyField('Book', through='Borrow', related_name='borrowers')
    
    def __str__(self):
        return self.username


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

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices= categ)
    image = models.ImageField(upload_to= 'uploadedPhotos/%y/%m/%d')
    borrowed = models.BooleanField(default= False)
    # borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books')
    
    def __str__(self):
        return self.title
    
# class Borrow(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     borrow_date = models.DateField(auto_now_add=True)
#     return_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return f'{self.user.username} borrowed {self.book.title}'
    
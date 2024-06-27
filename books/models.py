from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=50, default='Full name')
    email = models.CharField(max_length=50, default='email@email.com')
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    borrowed_books = models.ManyToManyField('Book', through='Borrow', related_name='borrowed_by_users')
    
    def __str__(self):
        return self.username

class Book(models.Model):
    categ = [
        ('Classic', 'Classic'),
        ('Fiction', 'Fiction'),
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
    category = models.CharField(max_length=50, choices=categ)
    image = models.ImageField(upload_to='uploadedPhotos/%y/%m/%d')
    borrowed = models.BooleanField(default=False)
    borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='borrowed_books_set')
    
    def __str__(self):
        return self.title
    
    def is_borrowed_by(self, user):
        return self.borrower == user

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'
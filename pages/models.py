from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50, default='Full name')
    email = models.CharField(max_length=50, default='email@email.com')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
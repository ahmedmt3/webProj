from django.contrib import admin
from .models import Book, User

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'borrowed', 'category']
    list_editable = ['borrowed', 'category']

class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'username', 'email']


admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_header = 'Dashboard'
admin.site.site_title = 'Dashboard'
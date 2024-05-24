from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'username', 'email']

admin.site.register(User, UserAdmin)
admin.site.site_header = 'Dashboard'
admin.site.site_title = 'Dashboard'
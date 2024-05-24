from django.shortcuts import render
from .models import User

def index(request):
    if(request.method == 'POST'):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = User(
                fullname= fullname, 
                email = email, 
                username= username, 
                password= password
            )
        data.save()
    
    return render(request, 'pages/signup.html')

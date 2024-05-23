from django.shortcuts import render
from django.http import HttpResponse

def index(reguest):
    return render(reguest, 'pages/index.html')

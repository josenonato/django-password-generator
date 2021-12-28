from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    
    vCharacters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        vCharacters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    
    if request.GET.get('special'):
        vCharacters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('number'):
        vCharacters.extend(list('1234567890'))

    vLength = request.GET.get('length',default=14)
    vPassword=''
    for x in range(int(vLength)):
        vPassword += random.choice(vCharacters)
    return render(request,'generator/password.html',{'password': vPassword})

def about(request):
    return render(request,'generator/about.html')

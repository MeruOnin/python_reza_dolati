from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

# ایمیل و رمز عبور معتبر
VALID_EMAIL = "heidariasan03@gmail.com"
VALID_PASSWORD = "Hossein2022"

def index(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            messages.success(request, 'ورود شما موفقیت آمیز بود')
        else:
            messages.error(request, 'ایمیل یا رمز عبور اشتباه است')
        return redirect('index')
    else:
        return redirect('index')


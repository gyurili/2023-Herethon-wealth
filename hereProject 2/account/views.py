from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

#
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('health:main')
        else:
            return render(request, 'login.html', {'error': '입력한 내용을 다시 확인해주세요.'})
    else: 
        return render(request, 'login.html')
    
def logout_view(request):
    auth.logout(request)
    return redirect('login_view')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            auth.login(request, user)
            return render(request, 'login.html')
        else:
            return render(request, 'signup.html', {'error': '비밀번호를 동일하게 입력하세요.'})
    
    return render(request, 'signup.html')

def poppage(request):
    return render(request, 'poppage.html')

def login1(request):
    return render(request, 'login1.html')

def face(request):
    return render(request, 'face.html')
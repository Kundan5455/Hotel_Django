from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login
# Create your views here.

def home(request):
    return render (request , 'home.html')


def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('passowrd')

        user_obj = User.objects.filter(username=username)
        
        print("USER---->",user_obj)

        if not user_obj.exists():
            messages.warning(request, "User Not Found !!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, "Invalid Password !!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        login(request, user_obj)
        return redirect ('/')

    return render(request, 'login.html')


def register_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('passowrd ')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, "User already Exist")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        user = User.objects.create (username=username )
        user.set_password(password)
        user.save()
        return redirect ('/')

    return render(request, 'register.html')
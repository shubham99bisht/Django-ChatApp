from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist! Please try some other username.")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!")
        
        elif len(username)>20 and not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric and under 20 charcters.")    

        elif password1 != password2:
           messages.error(request, "Passwords don't match")
        
        else:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, "SignUp succesful! Login to continue")
            return redirect('login')
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    messages.success(request, "SignOut succesful!")
    return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from authentication.models import CustomUser
from django.contrib.auth import login, authenticate, logout

User =get_user_model

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if user.is_active:
            login(request, user)
            messages.info(request, 'Login successful')
            return redirect('index')
           
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('authentication:user_login')
    return render(request, 'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        first_name= request.POST.get('first_name')
        second_name= request.POST.get('second_name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        password2= request.POST.get('password2')
        photo= request.POST.get('photo')

        if password == password2:
            if CustomUser.objects.filter(email = email).exists():
                messages.info(request, 'Email already exist')
                return redirect('authentication:signup')
            elif CustomUser.objects.filter(username = username).exists():
                messages.info(request, 'Username already exist')
                return redirect('authentication:signup')
            else:
                user_data = CustomUser(username = username, first_name = first_name,
                                         second_name = second_name, email = email,
                                         password = password, photo = photo)
                user_data.set_password(password)
                user_data.save()
                messages.info(request, 'You successfully signed up! Signin to continue')
                return redirect('authentication:user_login')
        else:
            messages.info(request, 'Password not match')
            return redirect('authentication:signup')
            
    return render(request, 'authentication/signup.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out. Login again!')
    return redirect('authentication:user_login')
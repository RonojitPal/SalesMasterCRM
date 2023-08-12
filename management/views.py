from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have Logged In!")
            return redirect('home')
        else:
            messages.success(request, "Error Logging In, Please Try Again!")
            return redirect('home')
    else:
        return render(request, 'homepage.html', {})

#def login_user(request):
    #return render(request,)


def logout_user(request):

    logout(request)
    messages.success(request, "You have been Logged Out!")
    return redirect('home')


def register_user(request):

    return render(request, 'register.html', {})



    

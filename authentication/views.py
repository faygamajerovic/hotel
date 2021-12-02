from django.contrib import auth
from django.contrib.auth.signals import user_logged_out
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from authentication.models import User
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm



def signin(request):


    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, 'pages/login.html')



def signup(request):

    signup_form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            user= form.cleaned_data.get('username')

            print(f"Sign Up successfully for the user: {user}")

            return redirect('login')


    context = {
        'form' : signup_form
    }
    return render(request, 'pages/register.html', context=context)

def signout(request):

    logout(request)

    return redirect("home")

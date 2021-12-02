from django.contrib import auth
from django.contrib.auth.signals import user_logged_out
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignupForm

User = get_user_model()


def signin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, 'pages/login.html')


def signup(request):

    signup_form = UserSignupForm()

    if request.method == "POST":

        form = UserSignupForm(request.POST)

        if form.is_valid():

            form.save()

            user = form.cleaned_data.get('username')

            print(f"Sign Up successfully for the user: {user}")

            return redirect('login')

    context = {
        'form': signup_form
    }
    return render(request, 'pages/register.html', context=context)


def signout(request):

    logout(request)

    return redirect("home")

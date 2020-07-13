from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    # return HttpResponse("Hello World")
    return render(request, "index.html", {})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to success page
    else:
        # Return invalid login error message
        return HttpResponse("Login Error")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})
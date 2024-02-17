from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import name_data
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def autho(request):
    username = 'kunal'
    return render(request, 'signup.html', {'user': username})


def sign(request):
    success = None
    current_page = request.path
    if current_page == "/login/":
        page_path = "/sign-up/"
        page_name = "Sign-up"
    elif current_page == "/sign-up/":
        page_path = "/login/"
        page_name = "Login"

    if request.method == "POST":
        name = request.POST.get('name')
        user = request.POST.get('user')
        passwords = request.POST.get('pass')
        if request.path == "/sign-up/":
            user_created = User.objects.create_user(user, "", passwords, first_name=name)
            if(user_created):
                success = f"Account created for {user}. Ready to go!"

    return render(request, 'signup.html',{'success':success, 'page_path':page_path, 'page_name': page_name})

def login_view(request):
    success = None
    current_page = request.path
    if current_page == "/login/":
        page_path = "/sign-up/"
        page_name = "Sign-up"
    elif current_page == "/sign-up/":
        page_path = "/login/"
        page_name = "Login"

    if request.method == "POST":
        users = request.POST.get('user')
        passwords = request.POST.get('pass')
        user = authenticate(username=users, password=passwords)
        if user is not None:
            login(request, user)
            return HttpResponse("Good guy come in")
        else:
            return HttpResponse("User doesn`t exist!")

    return render(request, 'login.html',{'success': success, 'page_path':page_path, 'page_name': page_name})


def logout_view(request):
    logout(request)
    if logout(request):
        val = "You are logged out!"
    return HttpResponseRedirect("/login/")


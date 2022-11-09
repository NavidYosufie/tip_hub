from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def register(request):
    context = {"errors": []}
    if request.user.is_authenticated:
        return redirect("home:home")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")

        if password_1 != password_2:
            context["errors"].append("this password not set please your password set")
            return render(request, "register.html", context)

        user = User.objects.create_user(username=username, email=email, password=password_2)
        login(request, user)
        return redirect("home:home")

    return render(request, "register.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("home:home")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:home")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("home:home")
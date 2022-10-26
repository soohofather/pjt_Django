from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):

    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect("accounts:login")
    else:
        signup_form = CustomUserCreationForm()
    context = {
        "signup_form": signup_form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):

    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect("reviews:index")
    else:
        login_form = AuthenticationForm()
    context = {
        "login_form": login_form,
    }

    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("reviews:index")


@login_required
def detail(request, pk):

    user = get_user_model().objects.get(pk=pk)

    context = {
        "user": user,
    }

    return render(request, "accounts/detail.html", context)


@login_required
def update(request):

    if request.method == "POST":
        user_update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        user_update_form = CustomUserChangeForm(instance=request.user)
    context = {
        "user_update_form": user_update_form,
    }

    return render(request, "accounts/update.html", context)


def password(request):

    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect("reviews:index")
    else:
        password_form = PasswordChangeForm(request.user)

    context = {
        "password_form": password_form,
    }

    return render(request, "accounts/password.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("reviews:index")

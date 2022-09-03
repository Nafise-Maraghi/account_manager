from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import SignupForm, LoginForm, ChangePasswordForm
from .models import User


@csrf_exempt
def login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user:
            auth_login(request, user)

            return HttpResponse("Logged in Successfully.", status=200)

        return render(request, 'login_failed.html', {"form": LoginForm()})

    elif request.method == "GET":
        return render(request, 'login.html', {"form": LoginForm()})


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first.')

        auth_logout(request)
        return HttpResponse('Logged out successfully.')

    return HttpResponse('Only post method is  allowed.')


@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            user_name = form.cleaned_data["username"]

            return HttpResponse(f"Welcome {user_name}!")

        else:
            return render(request, 'signup.html', {'form': form})

    elif request.method == "GET":
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})


@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ChangePasswordForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()

                return HttpResponse('Password changed successfully.')
        else:
            return HttpResponse('Please login first.')

    elif request.method == "GET":
        return render(request, 'change_password.html', {"form": ChangePasswordForm(request.user)})


@csrf_exempt
def show_all(request):
    if request.method == "GET":
        if request.user.is_authenticated and request.user.is_staff:
            users = User.objects.all()

            return render(request, 'show_all.html', {"users": users})

        else:
            return HttpResponse("Please login with a staff account.")

    return HttpResponse('Only get method is  allowed.')

# :)
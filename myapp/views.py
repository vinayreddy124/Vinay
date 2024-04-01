from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import DealerSignupForm, UserSignupForm
from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == CustomUser.Role.DEALER:
                return redirect('dealer_signup')
            else:
                return redirect('user_signup')
        else:
            pass
    return render(request, 'login.html')


def dealer_signup(request):
    if request.method == 'POST':
        form = DealerSignupForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = DealerSignupForm()
    return render(request, 'dealer_signup.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserSignupForm()
    return render(request, 'user_signup.html', {'form': form})
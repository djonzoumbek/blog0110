from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles:home')
        else:
            messages.error(request, 'Username or password is incorrect')

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('articles:home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login_user')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
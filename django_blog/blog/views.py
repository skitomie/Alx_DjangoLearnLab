from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = request.user
        user.email = email
        user.save()
        return redirect('profile')
    return render(request, 'profile.html')

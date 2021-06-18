from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import CustomUserModel
from .forms import CustomUserForm




def login_view(request):
    if request.method == 'POST':
        form = CustomUserForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('conspect:lessons_tmp')
    form = CustomUserForm()
    return render(request, 'login.html', {'form': form,
                                          })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('conspect:home')
    return render(request, 'logout.html', {})



















from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import *


def LoginView(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('crm:crm-dashboard')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('crm:crm-dashboard')
    context['form'] = form

    return render(request, 'useractions/login.html', context)

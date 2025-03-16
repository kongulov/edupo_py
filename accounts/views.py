from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
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


def logout_view(request):
    logout(request)
    return redirect('accounts:sign-in')


def signup_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('accounts:crm-dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        co_form = CompanyRegistrForm(request.POST)
        if form.is_valid() and co_form.is_valid():
            user = form.save(commit=False)
            user.usertype = 1
            user.is_active = True
            user.created_date = timezone.now()
            user.save()
            company = co_form.save(commit=False)
            company.package_company = 1
            company.owner = user
            company.save()

            user = form.save(commit=False)
            user.company = company
            user.save()
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            return redirect('accounts:sign-in')
    else:
        form = SignupForm()
        co_form = CompanyRegistrForm()
    context['form'] = form
    context['co_form'] = co_form
    return render(request, 'useractions/registration.html', context)


def MyProfileView(request):
    context = {}
    return render(request, 'settings/my-profile/my-account.html', context)

@login_required(login_url='/sign-in/')
def ProfileUpdateView(request):
    context = {}

    obj = request.user
    context['obj'] = obj

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile information has been successfully updated.')
            return redirect('accounts:my-profile')
    else:
        form = EditProfileForm(instance=obj)
    context['form'] = form
    return render(request, 'settings/my-profile/edit-profile.html', context)

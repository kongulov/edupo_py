from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from crm.forms import *


@login_required(login_url='/sign-in/')
def DashboardView(request):
    context = {}

    return render(request, 'home/dashboard.html', context)


@login_required(login_url='/sign-in/')
def CustomersView(request):
    context = {}
    context['customers_list'] = Customers.objects.filter(company=request.user.company)
    return render(request, 'crm/customers/customer-list.html', context)


@login_required(login_url='/sign-in/')
def CustomerAddView(request):
    context = {}
    if request.method == 'POST':
        form = CustomerAddForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.company = request.user.company
            customer.save()
            messages.success(request,
                             'Təbriklər,uğurla qeydiyyatdan keçdiniz!Xahiş edirik mailinizə gələn mesajı təsdiq edəsiniz!')
            return redirect('crm:customers')
    else:
        form = CustomerAddForm()
    context['form'] = form
    return render(request, 'crm/customers/customer-add.html', context)

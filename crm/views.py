from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from crm.forms import *


@login_required(login_url='/sign-in/')
def DashboardView(request):
    context = {}

    return render(request, 'home/dashboard.html', context)


@login_required(login_url='/sign-in/')
def CustomersView(request):
    context = {}
    context['customers_list'] = Customers.objects.all()
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
                             'The new customer has been successfully added.')
            return redirect('crm:customers')
    else:
        form = CustomerAddForm()
    context['form'] = form
    return render(request, 'crm/customers/customer-add.html', context)


@login_required(login_url='/sign-in/')
def CustomerUpdateView(request, slug):
    context = {}

    obj = get_object_or_404(Customers, slug=slug)
    context['obj'] = obj

    if request.method == 'POST':

        form = CustomerUpdateForm(request.POST, instance=obj)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()

            messages.success(request,
                             'The customer information has been successfully updated.')
            return redirect('crm:customers')
    else:

        form = CustomerUpdateForm(instance=obj)
    context['form'] = form
    return render(request, 'crm/customers/customer-update.html', context)

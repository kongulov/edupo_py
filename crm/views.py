from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404

from crm.forms import *
from crm.models import *


@login_required(login_url='/sign-in/')
def DashboardView(request):
    context = {}

    return render(request, 'home/dashboard.html', context)


# Customers views
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


# end Customers views


# start Company views
def UserCompanyView(request):
    company_list = UserCompany.objects.filter(owner=request.user).annotate(
        last_contact_person_id=Max('user_company_contact__id')
    ).order_by('-id')
    contact_persons = {
        company.id: ContactPerson.objects.filter(id=company.last_contact_person_id).first()
        for company in company_list
    }

    context = {
        'company_list': company_list,
        'contact_persons': contact_persons
    }

    return render(request, 'crm/usercompany/usercompany-list.html', context)


@login_required(login_url='/sign-in/')
def UserCompanyAddView(request):
    context = {}
    if request.method == 'POST':
        form = UserCompanyAddForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            email = form.cleaned_data['email']
            phone = form.cleaned_data['mobile_number']
            name = form.cleaned_data['contact_person']
            position = form.cleaned_data['position']

            company.save()
            ContactPerson.objects.create(user_company=company, email=email, phone=phone, position=position, name=name),
            messages.success(request,
                             'The new company has been successfully added.')
            return redirect('crm:user-companies')
    else:
        form = UserCompanyAddForm()
    context['form'] = form
    return render(request, 'crm/usercompany/usercompany-add.html', context)


@login_required(login_url='/sign-in/')
def UserCompanyUpdateView(request, slug):
    context = {}

    obj = get_object_or_404(UserCompany, slug=slug)
    context['obj'] = obj

    if request.method == 'POST':

        form = UserCompanyUpdateForm(request.POST, instance=obj)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()

            messages.success(request,
                             'The company information has been successfully updated.')
            return redirect('crm:user-companies')
    else:

        form = UserCompanyUpdateForm(instance=obj)
    context['form'] = form
    return render(request, 'crm/usercompany/usercompany-update.html', context)


# end Company views


@login_required(login_url='/sign-in/')
def ContactView(request):
    contact_list = ContactPerson.objects.filter(user_company__owner__company=request.user.company)

    context = {
        'contact_list': contact_list
    }

    return render(request, 'crm/usercompany/contacts/contact-list.html', context)

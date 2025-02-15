import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Count, Subquery, OuterRef, Q
from django.db.models.functions import TruncDate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from accounts.forms import CompanyEditForm
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
    total_contracts = Order.objects.filter(
        user_company=OuterRef('pk'),
        status=5
    ).values('user_company').annotate(
        count=Count('id')
    ).values('count')
    company_list = UserCompany.objects.filter(owner=request.user).annotate(
        last_contact_person_id=Max('user_company_contact__id'),
        total_contracts=Subquery(total_contracts, output_field=models.IntegerField())
    ).distinct()

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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            position = form.cleaned_data['position']

            company.save()
            ContactPerson.objects.create(user_company=company, email=email, phone=phone, position=position,
                                         first_name=first_name, last_name=last_name),
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

# start ContactPerson views
@login_required(login_url='/sign-in/')
def ContactView(request):
    contact_list = ContactPerson.objects.filter(user_company__owner__company=request.user.company)

    context = {
        'contact_list': contact_list
    }

    return render(request, 'crm/usercompany/contacts/contact-list.html', context)


@login_required(login_url='/sign-in/')
def ContactPersonAddView(request):
    if request.method == 'POST':
        form = ContactPersonAddForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            contact.save()
            messages.success(request,
                             'The new contact has been successfully added.')
            return redirect('crm:contacts')
    else:
        form = ContactPersonAddForm()
    context = {
        'form': form
    }
    return render(request, 'crm/usercompany/contacts/contact-add.html', context)


@login_required(login_url='/sign-in/')
def ContactPersonUpdateView(request, slug):
    context = {}

    obj = get_object_or_404(ContactPerson, slug=slug)
    context['obj'] = obj

    if request.method == 'POST':

        form = ContactPersonUpdateForm(request.POST, instance=obj)

        if form.is_valid():
            company = form.save(commit=False)
            company.save()

            messages.success(request,
                             'The contact information has been successfully updated.')
            return redirect('crm:contacts')
    else:

        form = ContactPersonUpdateForm(instance=obj)
    context['form'] = form
    return render(request, 'crm/usercompany/contacts/contact-update.html', context)


# end ContactPerson views

# start Order views

def OrdersView(request):
    context = {}
    context['orders_list'] = Order.objects.filter(company=request.user.company)

    return render(request, 'crm/order/order-list.html', context)


@login_required(login_url='/sign-in/')
def OrderAddView(request):
    if request.method == 'POST':
        form = OrderAddForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.company = request.user.company
            order.author = request.user
            order.save()
            messages.success(request,
                             'The new order has been successfully added.')
            return redirect('crm:orders')
    else:
        form = OrderAddForm()
    context = {
        'form': form
    }
    return render(request, 'crm/order/order-add.html', context)


@login_required(login_url='/sign-in/')
def OrderUpdateView(request, slug):
    context = {}

    obj = get_object_or_404(Order, slug=slug)
    context['obj'] = obj

    if request.method == 'POST':

        form = OrderUpdateForm(request.POST, instance=obj)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            messages.success(request,
                             'The order information has been successfully updated.')
            return redirect('crm:orders')
    else:

        form = OrderUpdateForm(instance=obj)
    context['form'] = form
    return render(request, 'crm/order/order-update.html', context)


# end Order views

# start Task views

@login_required(login_url='/sign-in/')
def TaskView(request):
    context = {}
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    two_days_later = today + datetime.timedelta(days=2)

    task_lists = {
        'today_task_list': Task.objects.annotate(deadline_date=TruncDate('deadline')).filter(
            Q(author=request.user, deadline_date=today) | Q(set_today=True)
        ).order_by('-set_today', '-created_date'),
        'tomorrow_task_list': Task.objects.annotate(deadline_date=TruncDate('deadline')).filter(
            author=request.user, deadline_date=tomorrow, set_today=False
        ),
        'upcoming_task_list': Task.objects.annotate(deadline_date=TruncDate('deadline')).filter(
            author=request.user, deadline_date__gte=two_days_later, set_today=False
        ),
        'overdue_task_list': Task.objects.annotate(deadline_date=TruncDate('deadline')).filter(
            author=request.user, deadline_date__lt=today, set_today=False
        )
    }

    for key, task_list in task_lists.items():
        for task in task_list:
            if task.priority == 1:
                task.border_class = 'border-color-left-red'
            elif task.priority == 2:
                task.border_class = 'border-color-left-blue'
            else:
                task.border_class = 'border-color-left-green'

    context['today_task_list'] = task_lists['today_task_list']
    context['tomorrow_task_list'] = task_lists['tomorrow_task_list']
    context['upcoming_task_list'] = task_lists['upcoming_task_list']
    context['overdue_task_list'] = task_lists['overdue_task_list']
    return render(request, 'crm/task/task-list.html', context)


@login_required(login_url='/sign-in/')
def task_set_priority(request, slug):
    obj = get_object_or_404(Task, slug=slug)
    obj.set_today = not obj.set_today
    obj.save()

    return redirect('crm:tasks')


# start calendar view#
def calendar_view(request):
    context = {}
    if request.method == 'POST':
        form = CalendarEventAddForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.company = request.user.company
            calendar.author = request.user
            calendar.save()
            messages.success(request,
                             'The new event has been successfully added.')
            return redirect('crm:calendar')
    else:
        form = CalendarEventAddForm()
    context['form'] = form
    return render(request, 'crm/calendar/calendar-list.html', context)


def get_events(request):
    events = CalendarEvent.objects.all()
    events_list = [
        {
            "title": event.title,
            "start": event.start_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            "end": event.end_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            "description": event.content,
            "color": event.color
        } for event in events
    ]
    return JsonResponse(events_list, safe=False)


# end calendar view

# start company profile


@login_required(login_url='/sign-in/')
def CompanyProfileUpdateView(request):
    context = {}

    obj = request.user.company
    context['obj'] = obj

    if request.method == 'POST':
        form = CompanyEditForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'The company profile information has been successfully updated.')
            return redirect('crm:company-profile')
    else:
        form = CompanyEditForm(instance=obj)
    context['form'] = form
    return render(request, 'settings/company-profile.html', context)

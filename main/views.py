from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from main.forms import *
from main.models import *


def IndexView(request):
    context = {}

    return render(request, 'base.html', context)


def FaqView(request):
    context = {}
    context['faq_list'] = Faq.objects.filter(draft=True).order_by('place')
    return render(request, 'faq/faq-list.html', context)


@login_required
def TicketListView(request):
    context = {}
    if not request.user.is_superuser:
        context['tickets'] = Support.objects.filter(author=request.user).order_by('-created')
    if request.user.is_superuser:
        context['tickets'] = Support.objects.all().order_by('-created')
    return render(request, 'support/ticket-list.html', context)


def create_support_ticket(request):
    if request.method == 'POST':
        form = SupportForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.company = request.user.company
            data.author = request.user
            data.save()
            return redirect('main:ticket_list')
    else:
        form = SupportForm()

    return render(request, 'support/ticket-add.html', {'form': form})


@login_required
def TicketDetailView(request, ticket_id):
    ticket = get_object_or_404(Support, ticket_id=ticket_id)
    messages = ticket.messages.all()
    form = SupportTicketMessageForm()

    if request.method == "POST":
        form = SupportTicketMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.ticket = ticket
            message.sender = request.user
            message.save()
            return redirect('main:ticket_detail', ticket_id=ticket.ticket_id)

    return render(request, 'support/tiket-detail.html', {'ticket': ticket, 'messages': messages, 'form': form})

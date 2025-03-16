from django.urls import path

from main.views import *

app_name = 'main'

urlpatterns = [
    path('', IndexView, name='index'),
    path('faq/', FaqView, name='faq'),
    path('tickets/', TicketListView, name='ticket_list'),
    path('ticket-add', create_support_ticket, name='ticket-add'),
    path('ticket/<str:ticket_id>/', TicketDetailView, name='ticket_detail'),

]

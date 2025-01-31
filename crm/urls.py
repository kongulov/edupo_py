from django.urls import path

from crm.views import *

app_name = 'crm'

urlpatterns = [
    path('crm-dashboard', DashboardView, name='crm-dashboard'),
    # customers
    path('customers/', CustomersView, name='customers'),
    path('customer-add/', CustomerAddView, name='customer-add'),
    path('customer/<slug>/', CustomerUpdateView, name='customer-update'),

    # user companies

    path('companies/', UserCompanyView, name='user-companies'),
    path('company-add/', UserCompanyAddView, name='company-add'),
    path('company/<slug>/', UserCompanyUpdateView, name='company-update'),
    path('contacts', ContactView, name='contacts'),
    path('contact-add/', ContactPersonAddView, name='contact-add'),
    path('contact/<slug>/', ContactPersonUpdateView, name='contact-update'),

    # orders
    path('orders/', OrdersView, name='orders'),
    path('order-add/', OrderAddView, name='order-add'),
    path('order/<slug>/', OrderUpdateView, name='order-update'),

    # task
    path('tasks/', TaskView, name='tasks'),
    # calendar
    path('calendar/', calendar_view, name='calendar'),
    path('api/events/', get_events, name='get-events'),
    # path('order/<slug>/', OrderUpdateView, name='order-update'),

    # #     path('sertler-qaydalar', views.PrivacyView, name='privacy'),
    # #     path('istifadeci-huquqlari', views.UserRightsView, name='userrights'),
    # path('elaqe', ContactView, name='contact'),
    # path('telim/<slug>/', CourseDetailView, name='course_detail_view'),
]

from django.urls import path

from crm.views import *

app_name = 'crm'

urlpatterns = [
    path('crm-dashboard', DashboardView, name='crm-dashboard'),
    # customers
    path('customers/', CustomersView, name='customers'),
    path('customer-add/', CustomerAddView, name='customer-add'),
    path('customer/<slug>/', CustomerUpdateView, name='customer-update'),
    path('ajax/get-course-price/', get_course_price, name='get_course_price'),

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
    path('task/set_today/<slug>/', task_set_priority, name='task_set_priority'),
    path('task-add/', TaskAddView, name='task-add'),
    path('task/<slug>/', TaskUpdateView, name='task-update'),
    # calendar
    path('calendar/', calendar_view, name='calendar'),
    path('api/events/', get_events, name='get-events'),
    # path('order/<slug>/', OrderUpdateView, name='order-update'),
    # notification

    path('notification/detail/<path:slug>/', notification_detail_view, name='notification_detail_view'),
    path('notification/', notification_view, name='notification'),

    # settings

    path('settings/company-profile/', CompanyProfileUpdateView, name='company-profile'),
    path('settings/general-settings/', GeneralSettingsUpdateView, name='general-settings'),
    path('settings/course-list/', CourseListView, name='course-list'),
    path('settings/course-add/', CourseAddView, name='course-add'),
    path('settings/course/<slug>/', CourseUpdateView, name='course-update'),
    path('settings/user-list/', UserListView, name='user-list'),
    path('settings/user-add/', UserAddView, name='user-add'),
    path('settings/user/<slug>/', UserUpdateView, name='user-update'),
    path('settings/permission-settings/', PermissionManagementView, name='permisson-settings'),
    path('settings/privacy-settings/', PrivacyManagementView, name='privacy-settings'),
    #     path('sertler-qaydalar', views.PrivacyView, name='privacy'),
    # #     path('istifadeci-huquqlari', views.UserRightsView, name='userrights'),
    # path('elaqe', ContactView, name='contact'),
    # path('telim/<slug>/', CourseDetailView, name='course_detail_view'),
]

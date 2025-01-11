from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from crm.views import *



app_name = 'crm'

urlpatterns = [
    path('crm-dashboard', DashboardView, name='crm-dashboard'),
    path('customers', CustomersView, name='customers'),
    path('customer-add', CustomerAddView, name='customer-add'),
    # path('bloq/<slug>/', blog_detail_view, name='blog_detail_view'),
    # path('bloq/kateqoriya/<slug>/', category_view, name='category_view'),
    # path('korporativ-telimler', CorparateCourseView, name='corportecourse'),
    # path('haqqimizda', AboutView, name='about'),
    # #     path('faq/', views.FaqView, name='faq'),
    # #     path('sertler-qaydalar', views.PrivacyView, name='privacy'),
    # #     path('istifadeci-huquqlari', views.UserRightsView, name='userrights'),
    # path('elaqe', ContactView, name='contact'),
    # path('telim/<slug>/', CourseDetailView, name='course_detail_view'),
]

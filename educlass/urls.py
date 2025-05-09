from django.urls import path

from educlass.views import *

app_name = 'educlass'

urlpatterns = [
    path('educlass/', educlass_view, name='educlass_view'),
    path('educlass/course/', course_view, name='course_view'),

    path('educlass/course/course-add/', CourseAddView, name='course-add'),
    path('educlass/course/<slug>/', CourseUpdateView, name='course-update'),
    path('add-category/', create_category_ajax, name='create_category_ajax'),

    # path('sign-up/', signup_view, name='sign-up'),
    # path('sign-out/', logout_view, name='logout_view'),
    # path('my-profile/', MyProfileView, name='my-profile'),
    # path('edit-profile/', ProfileUpdateView, name='edit-profile'),
    # #
    # path('robots.txt', RedirectView.as_view(url=staticfiles_storage.url('robots.txt'), ), name="robots"),
    # path('telimler', CourseView, name='course'),
    # path('bloqlar', BlogView, name='blog'),
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

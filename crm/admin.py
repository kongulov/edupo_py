from django.contrib import admin

from .models import *


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customers._meta.get_fields()]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'title', 'deadline', 'set_today']


admin.site.register(UserCompany)
admin.site.register(Course)
admin.site.register(ContactPerson)
admin.site.register(Order)

admin.site.register(CalendarEvent)
admin.site.register(Notification)
admin.site.register(NotificationView)

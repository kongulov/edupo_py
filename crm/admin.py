from django.contrib import admin

from .models import *


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customers._meta.get_fields()]


admin.site.register(UserCompany)

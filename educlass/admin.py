from django.contrib import admin
from educlass.models import *


@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class ModelCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'level','status')

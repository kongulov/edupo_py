from django.contrib import admin
from educlass.models import *


@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class ModelCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'level', 'status')


@admin.register(Instructor)
class ModelInstructorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Class)
class ModelClassAdmin(admin.ModelAdmin):
    list_display = ('name',)

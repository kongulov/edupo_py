from django.contrib import admin

from main.models import *


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'place')


admin.site.register(Support)
admin.site.register(SupportTicketMessage)

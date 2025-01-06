from django.contrib import admin
# from accounts.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import _lazy_re_compile as _
from django.contrib.auth import get_user_model
from accounts.models import *

User = get_user_model()

admin.site.register(Company)
@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'activation_code', 'password_reset_code','password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'email', 'phone_number', 'password1', 'password2'),
        }),
    )
    # # The forms to add and change user instances
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    list_display = ('first_name', 'last_name','company','usertype', 'email', 'is_superuser', 'is_active')
    list_display_links = ('first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    # search_fields = ('first_name', 'last_name', 'email')
    # ordering = ('-date_joined',)
    # filter_horizontal = ('groups', 'user_permissions',)
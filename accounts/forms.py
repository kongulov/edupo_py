from django import forms
from PIL import Image
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.forms import widgets
from django.utils.translation import gettext_lazy as _

from accounts.models import *
from accounts.models import *

User = get_user_model()
from ckeditor.widgets import CKEditorWidget


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email')
    }
    ))

    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()

    password = forms.CharField(max_length=100, label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control password',
            'placeholder': _('Şifrə')
        }
    ))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError(_('Email or password is invalid'))
        return super(LoginForm, self).clean()

#
# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
#         'class': 'col-md-12 ',
#         'placeholder': 'Email',
#         'label': '',
#     }
#     ))
#     first_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Ad',
#         'autofocus': '',
#         'label': 'Ad',
#
#     }))
#     last_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Soyad',
#         'label': '',
#     }))
#
#     password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Şifrə',
#             'label': '',
#         }
#     ))
#     password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Şifrəni doğrula',
#             'label': '',
#         }
#     ))
#
#     class Meta:
#         model = MyUser
#         fields = ('usertype', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#
#         try:
#             match = MyUser.objects.get(email=email)
#         except User.DoesNotExist:
#             return email
#         raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#
#         try:
#             match = MyUser.objects.get(username=username)
#         except User.DoesNotExist:
#             return username
#         raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')
#
#     def __init__(self, *args, **kwargs):
#         super(SignupForm, self).__init__(*args, **kwargs)
#         self.fields['email'].label = ""
#         self.fields['password1'].label = ""
#         self.fields['password2'].label = ""
#         self.fields['first_name'].label = ""
#         self.fields['last_name'].label = ""
#
#
# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = (
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'adress',
#         )

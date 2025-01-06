from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import *

User = get_user_model()


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


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'label': 'Email',
    }
    ))
    first_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ad',
        'autofocus': '',
        'label': 'Ad',

    }))
    last_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Soyad',
        'label': '',
    }))

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifrə',
            'label': '',
        }
    ))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Şifrəni doğrula',
            'label': '',
        }
    ))

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Bu email artıq mövcuddur.Yenisini yoxlayın!')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Bu istifadəçi adı artıq mövcuddur.Yenisini yoxlayın!')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-type password"
        self.fields['first_name'].label = "First name"
        self.fields['last_name'].label = "Last name"


class CompanyRegistrForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'name',
            'tax_id',
        )

    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Company name'),
    }
    ))
    tax_id = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Tax ID'),
    }
    ))

    def __init__(self, *args, **kwargs):
        super(CompanyRegistrForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Company name"
        self.fields['tax_id'].label = "Tax ID"

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

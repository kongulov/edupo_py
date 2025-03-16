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


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'name',
            'tax_id',
            'company_logo',
            'email',
            'phone_number',
            'address',
            'website',
        )

    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Company name'),
    }))

    tax_id = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Tax ID'),
    }))

    company_logo = forms.ImageField(max_length=100, label='', widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': _('Company logo'),
    }))

    email = forms.EmailField(max_length=100, label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email'),
    }))

    phone_number = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Phone number'),
    }))

    address = forms.CharField(max_length=255, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Address'),
    }))

    website = forms.URLField(max_length=200, label='', widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': _('Website'),
    }))

    def __init__(self, *args, **kwargs):
        super(CompanyEditForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Company name"
        self.fields['tax_id'].label = "Tax ID"
        self.fields['company_logo'].label = "Company logo"
        self.fields['email'].label = "Email"
        self.fields['phone_number'].label = "Phone number"
        self.fields['address'].label = "Address"
        self.fields['website'].label = "Website"


class GeneralSettingsForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('language',)
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class UserAddForm(forms.ModelForm):
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
        fields = ('first_name', 'last_name', 'usertype', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            match = MyUser.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already registered.')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            match = MyUser.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('This username is already registered. Please to try again.')

    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-type password"
        self.fields['first_name'].label = "First name"
        self.fields['last_name'].label = "Last name"
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))

    first_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'autofocus': '',
    }))

    last_name = forms.CharField(max_length=1200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
    }))

    # password1 = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'New Password (leave blank to keep current password)',
    # }))
    #
    # password2 = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Confirm New Password',
    # }))

    # is_active = forms.BooleanField(
    #     label="Active",
    #     required=False,
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'form-check-input',
    #     }),
    #     initial=True
    # )

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'usertype', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance

        if MyUser.objects.filter(email=email).exclude(id=user.id).exists():
            raise forms.ValidationError('This email is already registered.')
        return email

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #
    #     if password1 and password2:
    #         if password1 != password2:
    #             raise forms.ValidationError("Passwords do not match.")
    #     elif password1 or password2:
    #         raise forms.ValidationError("Both password fields must be filled if you wish to change the password.")
    #
    #     return password2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"

        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'user_image',
            'position',
        )

    first_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('First name'),
    }))

    last_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Last name'),
    }))

    email = forms.EmailField(max_length=100, label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email'),
    }))

    phone_number = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Phone number'),
    }))
    user_image = forms.ImageField(max_length=100, label='', widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': _('Image'),
    }))
    position = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': '',
        'placeholder': _('Position'),
    }))


    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First name"
        self.fields['last_name'].label = "Last name"
        self.fields['email'].label = "Email"
        self.fields['phone_number'].label = "Phone number"
        self.fields['user_image'].label = "Image"
        self.fields['position'].label = "Position"

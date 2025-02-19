from django import forms

from .models import *


# start Customer forms
class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'stage',
            'course_or_trainings',
            'location',
            'gender',
            'next_step',
            'status',
            'price',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stage': forms.Select(attrs={'class': 'form-control'}),
            'course_or_trainings': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'next_step': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'stage',
            'course_or_trainings',
            'location',
            'gender',
            'next_step',
            'status',
            'price',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'stage': forms.Select(attrs={'class': 'form-control'}),
            'course_or_trainings': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'next_step': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


# end Customer forms

# start Customer forms

class UserCompanyAddForm(forms.ModelForm):
    class Meta:
        model = UserCompany
        fields = (
            'name',
            'industry',
            'first_name',
            'last_name',
            'position',
            'email',
            'mobile_number',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class UserCompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = UserCompany
        fields = (
            'name',
            'industry',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


# end Customer forms

# start Contact


class ContactPersonAddForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = [
            'user_company',
            'first_name',
            'last_name',
            'phone',
            'email',
            'position'
        ]
        widgets = {
            'user_company': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class ContactPersonUpdateForm(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = [
            'user_company',
            'first_name',
            'last_name',
            'phone',
            'email',
            'position'
        ]
        widgets = {
            'user_company': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


# end Contact forms

# start Order forms

class OrderAddForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user_company',
            'status',
            'contact_person',
            'course',
            'participants',
        ]
        widgets = {
            'user_company': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'contact_person': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'participants': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'user_company',
            'status',
            'contact_person',
            'course',
            'participants',
        ]
        widgets = {
            'user_company': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'contact_person': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'participants': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


# end Order forms


# calendar event

from django import forms
from .models import CalendarEvent


class CalendarEventAddForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = [
            'title',
            'content',
            'event_type',
            'location',
            'attendees',
            'start_datetime',
            'end_datetime',
            'color',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'attendees': forms.EmailInput(attrs={'class': 'form-control'}),
            'start_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

# end calendar event
#task add form
class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'task_type',
            'deadline',
            'priority',
            'status',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'task_type': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'task_type',
            'deadline',
            'priority',
            'status',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'task_type': forms.Select(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})
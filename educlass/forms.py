from django import forms
from .models import *

# course add form
class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'category',
            'level',
            'status',
            'duration',
            'duration_type',
            'description',

        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        if company:
            self.fields['category'].queryset = Category.objects.filter(company=company)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'category',
            'level',
            'status',
            'duration',
            'duration_type',
            'description',

        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        if company:
            self.fields['category'].queryset = Category.objects.filter(company=company)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})
from django import forms
from .models import *

class SupportTicketMessageForm(forms.ModelForm):
    class Meta:
        model = SupportTicketMessage
        fields = ['message', 'file']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Type your message...'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['title', 'ticket_type', 'status', 'priority', 'file','content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the issue...'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-6'})
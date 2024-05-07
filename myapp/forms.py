from django.forms import ModelForm
from .models import Contact
from django import forms

class FormContact(ModelForm):
    class Meta:
        model = Contact
        exclude = ['id', 'tanggal']

        widgets = {
            'name': forms.TextInput({'class': 'form-control'}),
            'email': forms.TextInput({'class': 'form-control'}),
            'message': forms.Textarea({'class': 'form-control'}),
        }
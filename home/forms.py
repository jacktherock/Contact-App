from django import forms
from django.forms import fields, widgets
from .models import contact

class RegisterContact(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name', 'mobile_no']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name':'Contact Name',
            'mobile_no':'Mobile Number'
        }
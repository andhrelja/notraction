from django import forms
from .models import Driver
from events.forms import DateInput


class DriverModelForm(forms.ModelForm):
    
    class Meta:
        model = Driver
        fields = (
            'first_name',
            'last_name',
            'birth_date',
            'driver_image',
            'email',
            'phone',
            'city',
        )

        widgets = {
            'first_name'    : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name'     : forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date'    : DateInput(attrs={'class': 'form-control'}),
            'driver_image'  : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control'}),
            'city'          : forms.Select(attrs={'class': 'custom-select'}),
        }

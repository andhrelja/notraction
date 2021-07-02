from django import forms
from django.core.exceptions import ValidationError

from drivers.models import Driver
from .models import Car, Manufacturer


class CarModelForm(forms.ModelForm):
    make = forms.ModelChoiceField(label="Proizvođač", queryset=Manufacturer.objects.all(),
        widget=forms.Select(attrs={'class': "custom-select"}))
    driver = forms.ModelChoiceField(label="Vozač", queryset=Driver.objects.all(), empty_label=None, required=True,
        widget=forms.Select(attrs={'class': "custom-select", 'readonly': True}))
    active = forms.BooleanField(label="Aktivan", required=False,
        widget=forms.CheckboxInput(attrs={'class': ""}))

    class Meta:
        model = Car
        fields = (
            'driver',
            'image',
            'description',
            'make',
            'model',
            'year',
            'horse_power',
            'capacity',
            
        )

        widgets = {
            'image'         : forms.ClearableFileInput(attrs={'class': "form-control"}),
            'model'         : forms.Select(attrs={'class': "custom-select"}),
            'horse_power'   : forms.NumberInput(attrs={'class': "form-control"}),
            'capacity'      : forms.Select(attrs={'class': "custom-select"}),
            'year'          : forms.Select(attrs={'class': "custom-select"}),
            'description'   : forms.Textarea(attrs={'class': "form-control"})            
        }
    
    def __init__(self, *args, **kwargs):
        create = kwargs.pop('create')
        if create:
            driver = kwargs.pop('driver')
            super(CarModelForm, self).__init__(*args, **kwargs)
            self.fields['driver'].queryset = driver
            self.fields['active'].widget = forms.HiddenInput()
        else:
            driver = kwargs.pop('driver')
            make = kwargs.pop('make')
            active = kwargs.pop('active')
            super(CarModelForm, self).__init__(*args, **kwargs)
            self.fields['driver'].initial = driver.pk
            self.fields['make'].queryset = make
            self.fields['make'].empty_label = None
            self.fields['active'].initial = active

    def clean_driver(self):
        cleaned_data = super(CarModelForm, self).clean()
        driver = cleaned_data['driver']
        if driver.cardriver_set.filter(active=True).count() > 1:
            self.add_error('driver', error="Vozač već vozi jedan automobil")

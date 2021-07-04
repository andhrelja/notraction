from django import forms

from drivers.models import Driver
from .models import Car, Manufacturer


class CarModelForm(forms.ModelForm):
    make = forms.ModelChoiceField(label="Proizvođač", queryset=Manufacturer.objects.all(),
        widget=forms.Select(attrs={'class': "custom-select", 'onclick': "toggleModels()"}))
    driver = forms.ModelChoiceField(label="Vozač", queryset=Driver.objects.all(), empty_label=None, required=False,
        widget=forms.Select(attrs={'class': "custom-select", 'disabled': True}))
    active = forms.BooleanField(label="Aktivan", required=False,
        widget=forms.CheckboxInput())

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
            super(CarModelForm, self).__init__(*args, **kwargs)
            self.initial['active'] = True
            # self.fields['active'].widget = forms.HiddenInput()
        else:
            driver = kwargs.pop('driver')
            models = kwargs.pop('models')
            active = kwargs.pop('active')
            super(CarModelForm, self).__init__(*args, **kwargs)
            self.fields['model'].queryset = models
            self.initial['driver'] = driver
            self.initial['make'] = self.instance.model.manufacturer
            self.initial['active'] = active

    def clean_driver(self):
        cleaned_data = super(CarModelForm, self).clean()
        driver = cleaned_data['driver']
        if not driver:
            driver = self.initial['driver']

        car_driver = driver.cardriver_set.filter(active=True)
        if car_driver.count() >= 1:
            car = car_driver[0].car
            self.add_error('driver', error="Vozač već vozi {}".format(car.get_full_name()))

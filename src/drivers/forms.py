from django import forms
from .models import Driver
from events.models import County, City
from events.forms import DateInput


class DriverModelForm(forms.ModelForm):
    # TODO: Add Countries
    county = forms.ModelChoiceField(label="Županija", queryset=County.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-select', 'onchange': 'toggleCities()'}))

    class Meta:
        model = Driver
        fields = (
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'driver_image',
            'email',
            'phone',
            'county',
            'city',
            'categories',
        )

        widgets = {
            'first_name'    : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name'     : forms.TextInput(attrs={'class': 'form-control'}),
            'gender'        : forms.Select(attrs={'class': 'custom-select'}),
            'birth_date'    : DateInput(attrs={'class': 'form-control'}),
            'driver_image'  : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email'         : forms.EmailInput(attrs={'class': 'form-control'}),
            'phone'         : forms.TextInput(attrs={'class': 'form-control'}),
            'city'          : forms.Select(attrs={'class': 'custom-select'}),
            'categories'    : forms.SelectMultiple(attrs={'class': 'custom-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(DriverModelForm, self).__init__(*args, **kwargs)
        if kwargs['instance']:
            driver = kwargs['instance']
            self.fields['county'].initial = driver.city.county
            self.fields['city'].queryset = City.objects.filter(county=driver.city.county)
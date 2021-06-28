from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'driver',
            'image',
            'model',
            'horse_power',
            'capacity',
            'year',
            'description'
        )

        widgets = {
            'driver'        : forms.Select(attrs={'class': "custom-select"}),
            'image'         : forms.ClearableFileInput(attrs={'class': "form-control"}),
            'model'         : forms.Select(attrs={'class': "custom-select"}),
            'horse_power'   : forms.NumberInput(attrs={'class': "form-control"}),
            'capacity'      : forms.Select(attrs={'class': "custom-select"}),
            'year'          : forms.Select(attrs={'class': "custom-select"}),
            'description'   : forms.Textarea(attrs={'class': "form-control"})            
        }
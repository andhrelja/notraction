from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'horse_power',
            'capacity',
            'year',
            'description',
            'driver',
            'model',
            'image'
        )

        widgets = {
            'horse_power'   : forms.NumberInput(attrs={'class': "form-control"}),
            'capacity'      : forms.Select(attrs={'class': "custom-select"}),
            'year'          : forms.Select(attrs={'class': "custom-select"}),
            'description'   : forms.Textarea(attrs={'class': "form-control"}),
            'driver'        : forms.Select(attrs={'class': "custom-select"}),
            'model'         : forms.Select(attrs={'class': "custom-select"}),
            'image'         : forms.FileInput(attrs={'class': "form-control"})
        }
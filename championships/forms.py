from django import forms
from .models import Championship
from events.forms import DateInput

class ChampionshipModelForm(forms.ModelForm):

    class Meta:
        model = Championship
        ordering = ['-start_date']
        fields = (
            'name',
            'level',
            'start_date',
            'end_date',
            'city',
            'discipline'
        )

        widgets = {
            'name'          : forms.TextInput(attrs={'class': "form-control"}),
            'level'         : forms.TextInput(attrs={'class': "form-control"}),
            'start_date'    : DateInput(attrs={'class': "custom-select"}),
            'end_date'      : DateInput(attrs={'class': "form-control"}),
            'city'          : forms.Select(attrs={'class': "custom-select"}),
            'discipline'    : forms.Select(attrs={'class': "custom-select"}),
        }
from django import forms
from .models import Championship
from events.forms import DateInput

class ChampionshipModelForm(forms.ModelForm):

    class Meta:
        model = Championship
        ordering = ['-start_date']
        fields = (
            'name',
            'clubs_count',
            'club_position',
            'start_date',
            'end_date',
            'city',
        )

        widgets = {
            'name'          : forms.TextInput(attrs={'class': "form-control"}),
            'clubs_count'   : forms.NumberInput(attrs={'class': "form-control"}),
            'club_position' : forms.NumberInput(attrs={'class': "form-control"}),
            'start_date'    : DateInput(attrs={'class': "form-control"}),
            'end_date'      : DateInput(attrs={'class': "form-control"}),
            'city'          : forms.Select(attrs={'class': "custom-select"}),
        }
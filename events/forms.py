from django import forms
from .models import Event


class DateInput(forms.widgets.DateInput):
    input_type = "date"


class TimeInput(forms.widgets.TimeInput):
    input_type = "time"


class EventModelForm(forms.ModelForm):

    class Meta:
        model = Event
        ordering = ['start_date']
        fields = (
            'name',
            'cover',
            'description',
            'start_date',
            'end_date',
            'start_time',
            'end_time',
            'city'
        )

        widgets = {
            'name'          : forms.TextInput(attrs={'class': "form-control"}),
            'cover'         : forms.FileInput(attrs={'class': "form-control"}),
            'city'          : forms.Select(attrs={'class': "custom-select"}),
            'description'   : forms.Textarea(attrs={'class': "form-control"}),
            'start_date'    : DateInput(attrs={'class': "form-control"}),
            'end_date'      : DateInput(attrs={'class': "form-control"}),
            'start_time'    : TimeInput(attrs={'class': "form-control"}),
            'end_time'      : TimeInput(attrs={'class': "form-control"}),
        }
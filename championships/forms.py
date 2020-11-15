from django import forms
from .models import (
    Category, Championship, 
    ChampionshipType,
    DriverSubCategoryPosition,
    Organizer, SubCategory
)
from events.models import County
from events.forms import DateInput


class ChampionshipModelForm(forms.ModelForm):
    county              = forms.ModelChoiceField(label="Županija", queryset=County.objects.all(),
        widget=forms.Select(attrs={'class': 'custom-select', 'onchange': 'toggleCities()'}))    
    organizer           = forms.CharField(label="Organizator", max_length=64, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    championship_type   = forms.CharField(label="Tip prvenstva", max_length=128, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prvenstvo Hrvatske'}))


    class Meta:
        model = Championship
        ordering = ['-start_date']
        fields = (
            'name',
            'image',
            'organizer',
            'championship_type',
            'club_count',
            'club_position',
            'location',
            'start_date',
            'end_date',
            'county',
            'city',
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'image': forms.ClearableFileInput(attrs={'class': "form-control"}),
            'club_count': forms.NumberInput(attrs={'class': "form-control"}),
            'club_position': forms.NumberInput(attrs={'class': "form-control"}),
            'location': forms.TextInput(attrs={'class': "form-control"}),
            'start_date': DateInput(attrs={'class': "form-control"}),
            'end_date': DateInput(attrs={'class': "form-control"}),
            'city': forms.Select(attrs={'class': "custom-select"}),
        }

    def __init__(self, *args, **kwargs):
        super(ChampionshipModelForm, self).__init__(*args, **kwargs)
        if kwargs['instance']:
            championship = kwargs['instance']
            self.fields['county'].initial = championship.city.county

    def clean_championship_type(self):
        championship_type_name = self.cleaned_data.get("championship_type")
        championship_type, _ = ChampionshipType.objects.get_or_create(name=championship_type_name)
        return championship_type
    
    def clean_organizer(self):
        organizer_name = self.cleaned_data.get("organizer")
        organizer, _ = Organizer.objects.get_or_create(name=organizer_name)
        return organizer
    
    
class DriverSubCategoryPositionForm(forms.ModelForm):
    category     = forms.ModelChoiceField(label="Kategorija", queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'custom-select'}))
    
    class Meta:
        model = DriverSubCategoryPosition
        fields = (
            'category',
            'subcategory',
            'driver',
            'position',
            'championship'
        )
        widgets = {
            'driver'        : forms.Select(attrs={'class': 'custom-select'}),
            'subcategory'   : forms.Select(attrs={'class': 'custom-select'}),
            'position'      : forms.NumberInput(attrs={'class': 'form-control'}),
            'championship'  : forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(DriverSubCategoryPositionForm, self).__init__(*args, **kwargs)
        self.championship = self.initial['championship']
        
        self.fields['category'].queryset = self.championship.championship_type.category_set.all()
        self.fields['subcategory'].queryset = SubCategory.objects.filter(category__in=self.championship.championship_type.category_set.all())
        
        self.fields['category'].initial = self.fields['category'].queryset.first()
        self.fields['championship'].initial = self.championship


    def clean_championship(self):
        return self.championship
    
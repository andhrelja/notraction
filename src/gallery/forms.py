from django import forms
from .models import Gallery


class GalleryModelForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('name', 'images')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'images': forms.SelectMultiple(attrs={
                'class': "selectpicker",
                'title': "Odabir jedne ili više slika",
                'multiple': True
            })
        }

from django import forms
from .models import Gallery


class GalleryModelForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('name', 'images')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'images': forms.FileInput(attrs={
                'class': "form-control-file",
                'title': "Odaberi jednu ili više slika",
                'multiple': True
            })
        }

    def __init__(self, *args, **kwargs):
        if 'championship_pk' in kwargs:
            self.championship_pk = kwargs.pop('championship_pk')
        super(GalleryModelForm, self).__init__(*args, **kwargs)

from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm,
    UsernameField
)


class ProfileModelForm(UserCreationForm):

    profile_image = forms.ImageField(label="Profilna slika", widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = "form-control"
        self.fields['password2'].widget.attrs['class'] = "form-control"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        field_classes = {'username': UsernameField}
        widgets = {
            'profile_image' : forms.FileInput(attrs={'class': "form-control"}),
            'username'   : forms.TextInput(attrs={'class': "form-control"}),
            'first_name' : forms.TextInput(attrs={'class': "form-control"}), 
            'last_name'  : forms.TextInput(attrs={'class': "form-control"}),
            'email'      : forms.EmailInput(attrs={'class': "form-control"}),
        }


class LoginForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control"
        self.fields['password'].widget.attrs['class'] = "form-control"

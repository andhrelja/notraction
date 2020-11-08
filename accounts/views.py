from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .models import Profile
from .forms import ProfileModelForm, LoginForm
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile


class ProfileCreateView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfileModelForm
    success_message = "Registracija uspješno obavljena. Molimo prijavite se s novim računom"
    success_url = "/accounts/login/"

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user, profile_image=form.cleaned_data['profile_image'])
        return super(ProfileCreateView, self).form_valid(form)



class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileModelForm
    success_message = "Profil uspješno ažuriran"


class ProfileDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Profile
    success_message = "Profil uspješno izbrisan"
    success_url = "/"


class LoginView(auth_views.LoginView):
    form_class = LoginForm

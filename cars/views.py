from .models import Car
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Car
    success_message = "Automobil uspješno stvoren"


class CarUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Car
    success_message = "Automobil uspješno ažuriran"


class CarDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Car
    success_message = "Automobil uspješno izbrisan"
    success_url = '/cars/'

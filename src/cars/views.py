from .models import Car
from .forms import CarModelForm
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
    form_class = CarModelForm
    success_message = "Automobil uspješno stvoren"
    success_url = "/cars/"
    


class CarUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name_suffix = "_update_form"
    success_message = "Automobil uspješno ažuriran"
    


class CarDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Car
    success_message = "Automobil uspješno izbrisan"
    success_url = '/cars/'

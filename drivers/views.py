from .models import Driver
from .forms import DriverModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class DriverListView(ListView):
    model = Driver


class DriverDetailView(DetailView):
    model = Driver
    

class DriverCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Driver
    form_class = DriverModelForm
    success_message = "Vozač uspješno stvoren"


class DriverUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Driver
    form_class = DriverModelForm
    template_name_suffix = "_update_form"
    success_message = "Vozač uspješno ažuriran"


class DriverDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Driver
    success_message = "Vozač uspješno izbrisan"
    success_url = '/drivers/'

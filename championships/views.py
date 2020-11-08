from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Championship
from .forms import ChampionshipModelForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class ChampionshipListView(ListView):
    model = Championship


class ChampionshipDetailView(DetailView):
    model = Championship


class ChampionshipCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Championship
    form_class = ChampionshipModelForm
    success_message = "Prvenstvo uspješno stvoreno"


class ChampionshipUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Championship
    form_class = ChampionshipModelForm
    success_message = "Prvenstvo uspješno ažurirano"


class ChampionshipDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Championship
    success_message = "Prvenstvo uspješno izbrisano"
    success_url = "/championships/"

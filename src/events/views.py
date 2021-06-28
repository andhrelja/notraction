from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Event
from .forms import EventModelForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class EventListView(ListView):
    model = Event


class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventModelForm
    success_message = "Događaj uspješno stvoren"


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventModelForm
    success_message = "Događaj uspješno ažuriran"


class EventDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    success_message = "Događaj uspješno izbrisan"
    success_url = "/events/"

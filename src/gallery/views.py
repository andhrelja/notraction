from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Gallery
from .forms import GalleryModelForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class GalleryListView(ListView):
    model = Gallery

class GalleryDetailView(DetailView):
    model = Gallery

class GalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Gallery
    form_class = GalleryModelForm
    success_message = "Galerija uspješno stvorena"

class GalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Gallery
    form_class = GalleryModelForm
    success_message = "Galerija uspješno ažurirana"

class GalleryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Gallery
    success_message = "Galerija uspješno izbrisana"
    success_url = "/galleries/"

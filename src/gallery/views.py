from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Gallery, Image
from .forms import GalleryModelForm
from championships.models import Championship


class GalleryListView(ListView):
    model = Gallery

class GalleryDetailView(DetailView):
    model = Gallery

class GalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Gallery
    form_class = GalleryModelForm
    success_message = "Galerija uspješno stvorena"

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs.update({ 'championship_pk': self.kwargs['championship_pk']})
        return form_kwargs
    
    def post(self, request, **kwargs):
        FormClass = self.get_form_class()
        form = FormClass(request.POST)

        if form.is_valid():
            gallery = form.save()        
            championship = Championship.objects.get(pk=kwargs['championship_pk'])
            championship.albums.add(gallery)

            for i, image in enumerate(request.FILES.getlist('images')):
                alt = championship.name + f"_{i}"
                img = Image.objects.create(alt=alt, image=image)
                gallery.images.add(img)

            return redirect(gallery.get_absolute_url())
        return super().post(request)

class GalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Gallery
    form_class = GalleryModelForm
    success_message = "Galerija uspješno ažurirana"

    def __init__(self):
        return super().__init__()

    def form_invalid(self, form):
        FormClass = self.get_form_class()
        form = FormClass(self.request.POST)

        if form.is_valid():
            championship = self.object.championship
            for i, image in enumerate(self.request.FILES.getlist('images')):
                alt = championship.name + f"_{i}"
                img = Image.objects.create(alt=alt, image=image)
                self.object.images.add(img)
            
            return redirect(self.object.get_absolute_url())
        return super().form_invalid(form)


class GalleryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Gallery
    success_message = "Galerija uspješno izbrisana"
    success_url = "/galleries/"

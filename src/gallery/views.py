from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Gallery, Image
from .forms import GalleryModelForm, GalleryUpdateModelForm
from championships.models import Championship


class GalleryListView(ListView):
    model = Gallery

    def get_queryset(self):
        championship = Championship.objects.get(id=self.kwargs['championship_pk'])
        return championship.albums.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["championship"] = Championship.objects.get(id=self.kwargs['championship_pk'])
        return context
    
    

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["championship"] = Championship.objects.get(pk=self.kwargs['championship_pk'])
        return context
    
    
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
    form_class = GalleryUpdateModelForm
    success_message = "Galerija uspješno ažurirana"
    template_name = "gallery/gallery_update_form.html"

    def __init__(self):
        return super().__init__()
    
    def post(self, request, **kwargs):
        FormClass = self.get_form_class()
        form = FormClass(request.POST)
        self.object = self.get_object()

        if form.is_valid():
            championship = self.object.championship
            for i, image in enumerate(request.FILES.getlist('images')):
                alt = championship.name + f"-{i}"
                img = Image.objects.create(alt=alt, image=image)
                self.object.images.add(img)
            
            delete_images_ids = request.POST.getlist('delete_images')
            for i, image_id in enumerate(delete_images_ids):
                Image.objects.filter(id=image_id).delete()
            
            if delete_images_ids:
                self.success_message += ". Izbrisano {} slika".format(i + 1)
            messages.success(request, self.success_message)
            return redirect(self.object.get_absolute_url())
        return super().post(request, **kwargs)


class GalleryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Gallery
    success_message = "Galerija uspješno izbrisana"
    success_url = "/galleries/"

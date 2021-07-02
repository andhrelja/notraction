from .models import Car, Manufacturer
from .forms import CarModelForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from drivers.models import Driver, CarDriver


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Car
    form_class = CarModelForm
    success_message = "Automobil uspješno spremljen"
    success_url = "/cars/"

    def get_form_kwargs(self):
        kwargs = super(CarCreateView, self).get_form_kwargs()
        kwargs.update({
            'driver': Driver.objects.filter(id=self.kwargs['driver_pk']),
            'create': True
        })
        return kwargs
    
    def form_valid(self, form):
        driver = form.cleaned_data.pop('driver')
        make = form.cleaned_data.pop('make')
        active = form.cleaned_data.pop('active')
        response = super(CarCreateView, self).form_valid(form)
        CarDriver.objects.create(driver=driver, car=self.object)
        return response
    


class CarUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name_suffix = "_update_form"
    success_message = "Automobil uspješno ažuriran"
    
    def get_form_kwargs(self):
        kwargs = super(CarUpdateView, self).get_form_kwargs()
        car_driver = self.object.cardriver_set.first()
        kwargs.update({
            'driver': self.object.get_driver(),
            'active': car_driver.active,
            'make': Manufacturer.objects.filter(id=self.object.model.manufacturer.id),
            'create': False
        })
        return kwargs
    
    def form_valid(self, form):
        driver = form.cleaned_data.pop('driver')
        make = form.cleaned_data.pop('make')
        active = form.cleaned_data.pop('active')
        
        car_driver = self.object.cardriver_set.first()

        if not active:
            car_driver.active = False
            car_driver.date_deactivated = timezone.now()
        elif active:
            car_driver.active = True
            car_driver.date_deactivated = None

        car_driver.save()
        return super(CarUpdateView, self).form_valid(form)

class CarDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Car
    success_message = "Automobil uspješno izbrisan"
    success_url = '/cars/'

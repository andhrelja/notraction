from .models import Car, Manufacturer, Model
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


    def get_initial(self):
        initial = super().get_initial()
        initial.update({ 'driver': Driver.objects.get(id=self.kwargs['driver_pk']) })
        return initial

    def get_form_kwargs(self):
        kwargs = super(CarCreateView, self).get_form_kwargs()
        kwargs.update({ 'create': True })
        return kwargs
    
    def form_valid(self, form):
        response = super(CarCreateView, self).form_valid(form)
        driver = Driver.objects.get(id=self.kwargs['driver_pk'])
        CarDriver.objects.get_or_create(driver=driver, car=self.object)
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
            'models': Model.objects.filter(manufacturer=self.object.model.manufacturer),
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

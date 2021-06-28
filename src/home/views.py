from django.shortcuts import render
from django.views import View
from cars.models import Car, Model, Manufacturer
from events.models import Event
from championships.models import Championship


class HomeView(View):
    template_name = "home/index.html"

    def get(self, request):
        models = Model.objects.filter(car__in=Car.objects.all())
        championships = Championship.objects.all()[:4]
        events = Event.objects.all()[:4]
        
        context = {
            'car_manufacturers' : Manufacturer.objects.filter(model__in=models),
            'championships'     : championships,
            'events'            : events
        }
        return render(request, self.template_name, context)
    


class AboutView(View):
    template_name = "home/about.html"

    def get(self, request):
        # TODO: Update AboutView
        return render(request, self.template_name)

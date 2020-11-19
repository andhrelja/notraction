from django.shortcuts import render
from django.views import View
from cars.models import Car, Model, Manufacturer


class HomeView(View):
    template_name = "home/index.html"

    def get(self, request):
        models = Model.objects.filter(car__in=Car.objects.all())
        context = {
            'car_manufacturers' : Manufacturer.objects.filter(model__in=models)
        }
        return render(request, self.template_name, context)
    


class AboutView(View):
    template_name = "home/about.html"

    def get(self, request):
        # TODO: Update AboutView
        return render(request, self.template_name)

# TODO: Homepage
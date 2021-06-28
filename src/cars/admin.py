from django.contrib import admin
from .models import (
    Car,
    Model,
    Manufacturer
)

# Register your models here.
admin.site.register(Car)
admin.site.register(Model)
admin.site.register(Manufacturer)
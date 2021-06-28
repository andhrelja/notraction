from django.contrib import admin
from .models import (
    Event,
    City,
    County
)

# Register your models here.
admin.site.register(Event)
admin.site.register(City)
admin.site.register(County)

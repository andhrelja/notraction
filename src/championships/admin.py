from django.contrib import admin
from .models import (
    Championship,
    Category,
    SubCategory,
    Organizer,
    DriverSubCategoryPosition,
)

# Register your models here.
admin.site.register(Championship)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Organizer)
admin.site.register(DriverSubCategoryPosition)

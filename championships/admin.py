from django.contrib import admin
from .models import (
    Championship,
    CategoryDriverPosition,
    Discipline,
    Category
)

# Register your models here.
admin.site.register(Championship)
admin.site.register(CategoryDriverPosition)
admin.site.register(Discipline)
admin.site.register(Category)